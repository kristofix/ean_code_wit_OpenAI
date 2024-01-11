## Problem to solve: I only have the EAN number and I want the product name. EAN codebases don't have my product.

## Solution: Search for product name with google API and detect product name from first n result with OpenAI API

When you can't find product name in ean-search database, then it is possible to search for it in some popular search site like google. 
Here is sample usage with this code:

1. First we need to define how many results we want to consider from google results(num_results parameter). Here are first three results with links and description for the EAN code 5900694412941
   
URL: https://emokitty.pl/product-pol-35932-KLOCKI-KONSTRUKCYJNE-KID-BLOCKS-50-ELEMENTOW-WADER.html
Snippet: Kod produktu: 5900694412941. uniwersalny. Dostępność: status_icon 0 Produkt niedostępny. Możemy wysłać już: w czwartek. Sprawdź czasy i koszty wysyłki. Cena ...

URL: https://www.facebook.com/Babyland.md/photos/a.975381479195952/5172013062866085/?type=3
Snippet: Mar 15, 2022 ... ... 5900694412941 Заводской код: 41294 Размеры игрушки в сантиметрах: длина – 30, ширина – 12, высота – 25 Вес в граммах: 740 Цвет игрушки ...

URL: https://www.wader-zabawki.pl/kids-blocks-klocki-50-el.html
Snippet: Kids Blocks klocki 50 el. Kod: 41294; Producent: WADER; Kod producenta: 5900694412941; Waga: 0.74 kg. Czas realizacji: 5 dni. Wyjątkowe klocki Kids Blocks ...

2. Then we need to use the OpenAI API to analyze the results and extract the product name. From the top three results, we get 'Kids Blocks klocki 50 el. Wader'.
