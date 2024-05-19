# Лабораторная работа #1

В первой л\р необходимо разработать приложение:
Ввод диапазона IP-адресов.
На основании парсингаэтого диапазона рассчитать следующие параметры сети:
- а. Адрес сети
- б. broadcast адрес
- в. MAC-адрес вашего узла сети
- г.Маску сети

Алгоритм поиска маски на C#:

IPAddress beginIP - начальный ip-адрес
IPAddress endIP - конечный ip-адрес
--------------------------------
```
var begin = beginIP.GetAddressBytes();
var end = endIP.GetAddressBytes();
byte[] mask = new byte[4];
--------------------------------

bool edge = false;
 for(int i=0; i<4; i++)
  for(byte b=128; b>=1; b/=2){
    if(!edge && (begin[i]&b)==end[i]&b)) {
      mask[i]|=b;
    }
    else{
     edge=true;
     mask[i]=(byte)(mask[i]&~b);
    }
}
```




![image](https://github.com/danissimoae/AoCSaN-Sem4/assets/118019309/012515bb-bcf8-4be2-82b3-980547a8be6c)
