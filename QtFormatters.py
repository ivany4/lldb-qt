import lldb

def QUrl_SummaryProvider(valobj, internal_dict):
  return valobj.GetFrame().EvaluateExpression(value.GetName() + '.url((QUrl::FormattingOptions)QUrl::PrettyDecoded).toUtf8().data()');

def QString_SummaryProvider(valobj, internal_dict):
  def make_string_from_pointer_with_offset(F,OFFS, L):

    strval = '"'
    try:
      data = F.GetPointeeData(0, L)
      G = data.uint16
      for X in range(0, L):
        V = G[X]
        if V == 0:
          continue
        try:
          strval += chr(V)
        except NameError:
          strval += unichr(V)
    except Exception as e:
      pass
    strval = strval + '"'
    return strval.encode('utf-8')

  #qt4.8
  def qstring_summary(value):
    try:
      d = value.GetChildMemberWithName('d')
      offset = d.GetChildMemberWithName('alloc').GetValueAsUnsigned()
      size = d.GetChildMemberWithName('size').GetValueAsUnsigned()
      data = d.GetChildMemberWithName('data')
      return make_string_from_pointer_with_offset(data, offset, size)
    except Exception as e:
      return value
  
  return qstring_summary(valobj)

class QVector_SyntheticProvider:
  def __init__(self, valobj, internal_dict):
    self.valobj = valobj

  def num_children(self):
    try:
      s = self.valobj.GetChildMemberWithName('d').GetChildMemberWithName('size').GetValueAsUnsigned()
      return s
    except:
      return 0;

  def get_child_index(self,name):
    try:
      return int(name.lstrip('[').rstrip(']'))
    except:
      return None

  def get_child_at_index(self,index):
    if index < 0:
      return None
    if index >= self.num_children():
      return None
    if self.valobj.IsValid() == False:
      return None
    try:
      doffset = self.valobj.GetChildMemberWithName('d').GetChildMemberWithName('offset').GetValueAsUnsigned()
      type = self.valobj.GetType().GetTemplateArgumentType(0)
      elementSize = type.GetByteSize()
      return self.valobj.GetChildMemberWithName('d').CreateChildAtOffset('[' + str(index) + ']', doffset + index * elementSize, type)
    except:
      return None

class QList_SyntheticProvider:
  def __init__(self, valobj, internal_dict):
    self.valobj = valobj

  def num_children(self):
    try:
      listDataD = self.valobj.GetChildMemberWithName('p').GetChildMemberWithName('d')
      begin = listDataD.GetChildMemberWithName('begin').GetValueAsUnsigned()
      end = listDataD.GetChildMemberWithName('end').GetValueAsUnsigned()
      return (end - begin)
    except:
      return 0;

  def get_child_index(self,name):
    try:
      return int(name.lstrip('[').rstrip(']'))
    except:
      return None

  def get_child_at_index(self,index):
    if index < 0:
      return None
    if index >= self.num_children():
      return None
    if self.valobj.IsValid() == False:
      return None
    try:
      pD = self.valobj.GetChildMemberWithName('p').GetChildMemberWithName('d');
      pBegin = pD.GetChildMemberWithName('begin').GetValueAsUnsigned()
      pArray = pD.GetChildMemberWithName('array').GetValueAsUnsigned()
      pAt = pArray + pBegin + index
      type = self.valobj.GetType().GetTemplateArgumentType(0)
      elementSize = type.GetByteSize()
      voidSize = pD.GetChildMemberWithName('array').GetType().GetByteSize()
      return self.valobj.GetChildMemberWithName('p').GetChildMemberWithName('d').GetChildMemberWithName('array').CreateChildAtOffset('[' + str(index) + ']', pBegin + index * voidSize, type)
    except:
      return None

class QPointer_SyntheticProvider:
  def __init__(self, valobj, internal_dict):
    self.valobj = valobj

  def num_children(self):
    try:
      wp = self.valobj.GetChildMemberWithName('wp')
      d = wp.GetChildMemberWithName('d')
      if d.GetValueAsUnsigned() == 0 or d.GetChildMemberWithName('strongref').GetChildMemberWithName('_q_value').GetValueAsUnsigned() == 0 or wp.GetChildMemberWithName('value').GetValueAsUnsigned() == 0:
        return 0
      else:
        return 1
    except:
      return 0;

  def get_child_index(self,name):
    return 0

  def get_child_at_index(self,index):
    if index < 0:
      return None
    if index >= self.num_children():
      return None
    if self.valobj.IsValid() == False:
      return None
    try:
      type = self.valobj.GetType().GetTemplateArgumentType(0)
      return self.valobj.GetChildMemberWithName('wp').GetChildMemberWithName('value').CreateChildAtOffset('value', 0, type)
    except:
      return None
