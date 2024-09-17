# Материалы из книги:
### Майкл Фицджеральд - Регулярные выражения. Основы - 2015

## Для кого эта книга:
>Предполагаемые читатели книги - люди, которые за всю свою жизнь не написали 
еще ни одного регулярного выражения. Если вам уже приходилось сталкиваться с регулярными выражениями, но ваша практика работы с ними 
довольно ограниченна, то эта книга будет для вас полезной.

## Рекомендации по другим книгам:
> - Джеффри Фридла Регулярные выражения, 3-е издание (Символ-Плюс, 2008 г.)
> - Яна Гойвертса и Стивена Левитана Регулярнье выражения. Сборник рецептов, 2-е издание (Символ-Плюс, 2015 r.)

## Определения:
> ***Регулярные выражения:*** это специальные текстовые строки, которые используются 
в качестве шаблонов (образцов) для сопоставления с наборами других строк.

> ***Строковый литерал:*** это буквальное представление строки.

> ***Символьные классы:*** последовательность символов, заключенная в квадратные скобки, называется "символьным классом".

> ***Символьное сокращение или символьная маска:*** укороченное представление целых символьных классов.   
***Пример:*** \d является символьным сокращение символьного класса `[0-9]` 

# Метасимволы:
| символ | описание                                                                                                    |
|--------|-------------------------------------------------------------------------------------------------------------|
| `\`    | Служит для экранирования служебных символов например `\{` или же как часть метасимвола к примеру `\d`       |
| `^`    | Обозначает начало строки                                                                                    |
| `$`    | Обозначает конец строки                                                                                     |
| `.`    | Точка обозначает любой одиночный символ                                                                     |


# Символьные сокращения:
| символ   | описание                                                                                                    |
|----------|-------------------------------------------------------------------------------------------------------------|
| `\b`     | Граница слова.                                                                                              |
| `[\b]`   | Возврат на шаг (забой)                                                                                      |
| `\B`     | Не граница слова                                                                                            |
| `\cx`    | Управляющий символ из таблици `ASCII` начиная от `0` до `31`                                                |
| `\d`     | Обозначает любую одиночную цифру от `0` до `9`                                                              |
| `\d xxx` | Десятичное значение кода символа                                                                            |
| `\D`     | Обозначает любой символ не являющийся цифрой (любой символ кроме диапазона `0-9`)                           |
| `\f`     | Прогон страницы                                                                                             |
| `\h`     | Горизонтальный пробел                                                                                       |
| `\H`     | Не горизонтальный пробел                                                                                    |
| `\n`     | Перевод строки                                                                                              |
| `\r`     | Перевод каретки                                                                                             |
| `\o xxx` | Восьмеричное значение кода символа                                                                          |
| `\s`     | Пробел (пустой символ)                                                                                      |
| `\S`     | Не пробел (не пустой символ)                                                                                |
| `\t`     | Символ горизонтальной табуляции                                                                             |
| `\v`     | Символ вертикальной табуляции ( вертикальный пробел)                                                        |
| `\V`     | Не вертикальный пробел                                                                                      |
| `\w`     | Соответствует любому символу буквенному, цифирному или _ аналог `[_a-zA-Z0-9]`                              |
| `\W`     | Соответствует любому символу не входящему в буквенные, циферные или _ и  и является противоположностью `\w` |
| `\0`     | Пустой символ (Null)                                                                                        |
| `\x xx`  | Шестнадцатеричное значение кода символа                                                                     |
| `u xxxx` | Символ в кодировке Unicode                                                                                  |

# Символьные классы:
| символ  | описание                                                                                                                                                               |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `[0-9]` | Находит совпадение с элементами перечисленными в квадратных скобках. `[0-9]` так же можно представить в виде списка цифр `[0123456789]` и найдет любую одиночную цифру |
| `^`     | В контексте символьного класса указывается в самом начале и обозначает отрицание тоесть "найти любой символ не входящий в символьный класс"                            |

# Квантификаторы:
| символ       | описание                                                                                                        |
|--------------|-----------------------------------------------------------------------------------------------------------------|
| `{number}`   | Обозначает что предыдущий символ или группа символов должны повторяться `number` раза                           |
| `{min, max}` | Обозначает что предыдущий символ или группа символов должны повторяться минимум `min` раза и максимум `max` раз |
| `?`          | Означает что предыдущий символ должен повториться `0` или `1` раз                                               |
| `+`          | Означает что предыдущий символ должен повторяться `1` или более раз                                             |
| `*`          | Означает что предыдущий символ должен повторяться `0` или более раз                                             |

> __Квантификаторы__: это


# Захватывающие группы и обратные ссылки:
| символ          | описание                                                                                      |
|-----------------|-----------------------------------------------------------------------------------------------|
| `(Hello world)` | Создает группу символов которая доступна по ссылке `\index`                                   |
| `\| `           | Обозначает логическое `ИЛИ` то есть одно из двух возможных значений пример `(Hello \| hello)` |
| `\index`        | Обращение к соответствующей группе символов по ссылке где `index` это номер группы            |

> __Захватывающие группы__: это
