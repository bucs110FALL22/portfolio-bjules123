article = "With her family supporting her from the front row, Kim Kardashian took center stage at Dolce & Gabbana's Milan Fashion Week show. On Sept. 23, she appeared on the runway with Stefano Gabbana and Domenico Dolce during the finale of the event after they debuted a new spring-summer 2023 collection, a collaboration with the reality star. Kim wore a sleeveless gown covered in black Swarovski crystals in different dimensions to achieve a three dimensional texture, and her platinum blond hair styled in an updo. Kim's eldest three children North West, 9, Saint West, 6, and Chicago West, 4, plus mom Kris Jenner and sister Khloe Kardashian cheered her on from the front row. 'The most incredible show in Milan today!!' Kris wrote on Instagram. 'kimkardashian @dolcegabbana, perfection as always! So proud of you @kimkardashian!!! #MilanFashionWeek #CiaoKim #DolceandGabbana'The show opened to the sounds of camera clicks, light flashes and screams of 'We love you Kim! ELLE reported'. The show's models wore mostly black, white and silver looks with signature lace, crystal and leopard print embellishments as a black and white video of Kim eating spaghetti played in the background, the magazine said. North West, Kim Kardashian, Paris Fashion Week 2022. Kim Kardashian and North West Step Out at Paris Fashion Week. Kim curated the new collection with the brand, which recently unveiled its advertising campaign for it, titled 'Ciao Kim.' It features Kim wearing a black lace dress surrounded by paparazzi. 'Kim is the ultimate muse', the company said in a statement. 'Her confidence, independence, sense of style and sensuality have served as inspiration to Domenico Dolce and Stefano Gabbana in creating this Collection and revisiting their '90s and '00s archives. It is these very same legendary pieces that have inspired Kim so often throughout her own life and career, making this moment a dream come true'.Kim channels Marilyn Monroe in the ads, which were released four months after the SKIMS founder paid tribute to the late Hollywood icon at the 2022 Met Gala by dying her hair platinum blonde and wearing the dress the actress wore while singing 'Happy Birthday' to President John F. Kennedy in 1962. Kim's collaboration with Dolce & Gabbana also comes four months after the designers dressed the Kardashian-Jenner family and bride Kourtney Kardashian at her wedding to Travis Barker in Italy.Kim's Dolce & Gabbana catwalk appearance did not, however, mark her official runway modeling debut. That took place in July, at Balenciaga's fall/winter 2022 show during Paris Couture Fashion Week"

my_dictionary = { 
  "Kim": "The Queen of Instagram",
  "Dolce & Gabbana": "The Legendary Company",
  "Kourtney Kardashian" : "The oldest sister",
  "Travis Barker" : "The drummer",
  "West" : "(Kanye's Kid)",
  "Fashion Week" : "best week ever"
}

for key, value in my_dictionary.items():
  article = article.replace(key, value)

print(article)
