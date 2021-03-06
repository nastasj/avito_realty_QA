*У пользователя есть возможность авторизоваться на сайте через форму https://www.avito.ru/#login
В качестве логина можно использовать номер мобильного телефона или электронную почту.
В качестве пароля можно использовать цифры, буквы латинского языка и специальные символы. Допустимая длина пароля от 8 до 16 символов.*

**Задача** 

*Составить набор тестовых данных, при котором мы гарантированно будем знать, что авторизация работает.*
***
**Результат** 

Сначала я проанализировала требования и описала допустимые и недопустимые значения для тестируемого продукта, пользуясь техниками выделения классов эквивалентности и граничных значений (выделяла значения по краям и в середине допустимых и недопустимых интервалов значений).

<p align="center"><i>Возможные значения для тестирования формы авторизации</i><p/>

#### Логин

    I. Телефонный номер (предполагается, что телефонные номера — российские)
   
         a) Допустимые значения (x - цифры)
            1. +79xxxxxxxxx (символ „+” и 11 цифр, начиная с семерки)
            2. 89xxxxxxxxx (11 цифр, начиная с восьмерки)
            3. 9xxxxxxxxx (10 цифр, начиная с девятки)
           
         b) Недопустимые значения (x – цифры, y - буквы)
            1. null (пустое поле)
            1. xxxxxxxxx (строка цифр произвольной длины)
            2. yyyyyyy (строка букв произвольной длины)
            3. xxyyxxyyyyyxx (произвольная комбинация цифр и букв)
            4. ?**%?(_-=+./-:? (строка спецсимволов произвольной длины)
            5. +79xxx (символ „+” и 5 цифр, начиная с „79“)
            6. +79xxxxxxxx (символ „+” и 10 цифр, начиная с „79“)
            7. +79xxxxxxxxxx (символ „+” и 12 цифр, начиная с „79“)
            8. +79xxxxxxxxxxxxxxx (символ „+” и строка цифр длиной >12, начиная с „79“)
            9. +79xxyyxxyyyyyxxxy (символ „+” и произвольная комбинация цифр и букв, начиная с „79“)
            10. +79yyyyyyyyyyyy (символ „+” и строка букв произвольной длины, начиная с „79“)
            11. +79?**%**?_-=+./ (символ „+” и строка спецсимволов произвольной длины, начиная с „79“)
            12. +79?(xxx*?_xx-= (символ „+” и строка цифр и спецсимволов произвольной длины, начиная с „79“)
          
        + пункты 13-20 для кейса [89xxxxxxxxx] аналогичны пунктам 6-13
        + пункты 21-28 для кейса [9xxxxxxxxx] аналогичны пунктам 6-13
        
    II. E-mail
    
         a) Допустимые значения (x – латинские буквы, вместо .com может быть любой домен)
            1. x@domain.com (1 символ в локальной части)
            2. xxxxxxx@domain.com (32 символа в локальной части)
            3. xxxxxxxxxxx@domain.com (64 символа в локальной части)
            4. xxxxxxxxxxx@xxxxxxxx.com (254 символа в сумме в локальной и доменной части)
            5. xxx.2@domain.com.net
            6. xxx1@domain.com
            7. 1xxx@domain.com
            8. XXX@domain.com
            9. xxx+XXX@domain.com
            10. xxx_xxx@domain.com
            11. xxxx-xx@domain.com
            12. xxxx@domain-domain.com
           
         b) Недопустимые значения (x – латинские буквы, вместо .com может быть любой домен)
            1. null (пустое поле)
            2. @domain.com (нет символов в локальной части)
            3. xxx@ (нет символов в доменной части)
            4. @ (нет символов в локальной и доменной части)
            5. xxxxxxxxxxx@domain.com (65 символов в локальной части)
            6. xxxxxxxxxxx@xxxxxxxx.com (255 в сумме в локальной и доменной части)
            7. xxx xxxxx@domain.com (пробел в локальной части)
            8. xxxxxxxx@domain com (пробел вместо точки в домене)
            9. x..x@domain.com (две точки подряд в локальной части)
            10. xxxxx@domain.com. (email с точкой в конце домена)
            11. xxxxx@.domain.com (email с точкой в начале домена)
            12. xxxxx@domain..com (email с точкой перед доменным именем первого уровня)
            13. xxxx<>xx()@domain.com (запрещенные спецсимволы)

#### Пароль 

    a) Допустимые значения (x – латинские буквы)
        1. 1234XXxx (8 символов, используются цифры и латиница, оба регистра)
        2. 1234XXxx12xX (12 символов, используются цифры и латиница, оба регистра)
        3. 1234XXxx1234XXxx  (16 символов, используются цифры и латиница, оба регистра)
        4. 1234Xx%x (8 символов, используются все допустимые символы, оба регистра)
        5. 1234Xx%x12x& (12 символов, используются все допустимые символы, оба регистра)
        6. 1234Xx%x1234Xx%x (16 символов, используются все допустимые символы, оба регистра)

    b) Недопустимые значения (x – латинские буквы)
        1. null (пустое поле)
        2. %4Xx (4 символа, используются все допустимые символы, оба регистра)
        3. 1234Xx% (7 символов, используются все допустимые символы, оба регистра)
        4. 1234X1x%x1234Xx%2 (17 символов, используются все допустимые символы, оба регистра)
        5. 1234X1x%x1234Xx%2455xx*&^ (>17 символов, используются все допустимые символы, оба регистра)
        6. xxxxxxxxxxx (используются только латинские буквы, произвольная длина)
        7. 3357798098 (используются только цифры, произвольная длина)
        8. 455№»!778)% (используются только цифры и спецсимволы, произвольная длина)


Затем я сгенерировала набор комбинаций на основе попарного сочетания всех значений всех параметров с помощью инструмента PICT. Этот инструмент и техника pairwise testing позволили сократить количество необходимых тест-кейсов до 625, тем самым оптимизировав процесс тестирования.

<img src="https://user-images.githubusercontent.com/78635647/108240581-0a612280-715c-11eb-8bf6-e40128562c75.png" width="550">
<img src="https://user-images.githubusercontent.com/78635647/108240943-61ff8e00-715c-11eb-8902-3231855b79af.png" width="550">
