lovely_loveseat_description = "Härlig Kärlekssoffa i polyesterblandning. Ett träunderrede bär upp denna 81 cm höga, 102 cm breda och 76 cm djupa soffa. Finns i röd eller vit."

lovely_loveseat_price = 254.00


stylish_settee_description = "Stilfull Bänksoffa i svart konstläder. Slank och modern design på björkben. Mått: 75 cm hög, 139 cm bred och 71 cm djup."

stylish_settee_price = 180.50


luxurious_lamp_description = "Lyxig Lampa i glas och järn. Stående 91 cm hög, med en brun bas och en cremefärgad skärm, sprider den ett behagligt ljus."

luxurious_lamp_price = 52.15

sales_tax = 0.088

customer_one_total = 0

customer_one_itemization = ""

customer_one_itemization = lovely_loveseat_description + luxurious_lamp_description

customer_one_total = luxurious_lamp_price + lovely_loveseat_price

customer_one_tax = customer_one_total * sales_tax



print("varor för kund ett:", customer_one_itemization)
print("totalt för kund ett:", customer_one_total)