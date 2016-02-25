#include <QCoreApplication>
#include <QVector>
#include <QString>
#include <QList>
#include <QPointer>

int main(int argc, char *argv[])
{
   QCoreApplication a(argc, argv);

   QString s = "Hello World";

   QVector<int> vi;
   vi << 11;
   vi << 22;
   vi << 33;

   QVector<QString> vs;
   vs << "Hello";
   vs << "World";

   QVector<QVector<QString>> vvs;
   vvs << vs;
   vvs << vs;

   QList<int> li;
   li << 11;
   li << 22;
   li << 33;

   QList<QString> ls;
   ls << "Hello";
   ls << "World";

   QList<QList<QString>> lls;
   lls << ls;
   lls << ls;

   QPointer<QCoreApplication> ap;
   ap = &a;


   return a.exec();
}
