from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt

import sys
import random

from datetime import datetime
import pytz

#Add image dictionary + homepage of a beer icon

#To package: open cmd, type in auto-py-to-exe

City_List = {
    "Baker_Island" : ("Baker Island is an atoll; A ring-shaped island with a coral rim that has a lagoon in the middle",
                    "Baker Island is an uninhabited island used as a U.S. National Wildlife Refuge for several seabirds and shorebirds",
                    "Baker Island is largely inaccessible to the public, the exception being public visitations permitted by the U.S. Fish and Wildlife service"),

    "Howland_Island" : (
        "Howland Island is an uninhabited coral island shaped like a bean, north of the equator in the central Pacific Ocean",
        "Howland Island is best known as the island Amelia Earhart was flying towards but never reached during her planned round-the-world flight",
        "Howland Island has suffered from multiple invasive species. Black rats were first introduced to the island, then eradicated by feral cats introduced by the military, which in turn took 25 years to remove from the island"),

    "Pago_Pago" : (
        "The village Pago Pago is the capital of American Samoa and is home to one of the deepest natural deepwater harbors in the South Pacific Ocean",
        "Tuna exports make up a majority of the economic activity in Pago Pago. Famous tuna brands STARKIST and CHICKEN OF THE SEA are located in Pago Pago, at one point generating 446 million USD from exports alone.",
        "Despite the spelling, the city is pronounced as 'Pongo Pongo'"),

    "Alofi" : (
        "Alofi is the capital of the Pacific Ocean island nation Niue, and has the second smallest population size of any national capital city (approx. 640 people!).",
        "The island nation Niue, whose capital is Alofi, is a self-governing state in free association with New Zealand since October 1974. Niueans are recognized as New Zealand citizens.",
        "The island nation Niue, whose capital is Alofi, earns a portion of their income from internationally leasing their unique 4-digit telephone number, which is the shortest length a mobile number in the world can be!"
        ),

    "Swains_Island" : (
        "Swains Island is an atoll; A ring-shaped island with a coral rim that has a lagoon in the middle. This island is covered heavily with vegetation including 800 acres of coconut palm trees.",
        "Swains Island was named when in 1841 Captain William L. Hudson claimed to have found the island from coordinates provided by a certain Captain Swain of Nantucket. Who Captain Swain is however, has never been conclusively determined.",
        "Swains Island is largely uninhabited (A 2010 census counted 17 people, and a 2020 census counted 0 people) and can only be accessed by boat, either a private water craft or the Maine DOT Ferry Service."),

    "Honolulu" : (
        "Honolulu, which means 'calm port' in Hawaiian, is the capital and largest city in Hawaii, USA. It is a city with a favorable tropical climate, rich natural scenary and large beaches making it an extremely popular holiday destination, receiving 7000 - 11000 people everyday! In 2019 Honolulu received 60% of all total visitors to Hawaii by air!",
        "As an extremely popular tourist destination, Honolulu, Hawaii, brings in up to $10 billion every year to the local economy. Also of note, mid-2022 saw jobs in Hawaii in 'Food Services & Drinking' increase by 12.6%, and jobs in 'Accomodation' increase by 34.7%!",
        "Honolulu, Hawaii, houses the ONLY royal palace in the United States of America: the Iolani Palace. The palace served as the official residences of the monarchs starting with Kamehameha III. When Queen Liliʻuokalani and the monarch were overthrown in 1893, the palace became a capitol building for the government of Hawaii. Today, it is a National Historic Landmark open to visitors for tours!"
        ),

    "Waipahu" : (
        "Waipahu, Hawaii, is the location of a former sugarcane plantation owned by Oahu Sugar Company. The plantation included 943 field workers, majority of which were either Chinese or Japanese, and ran a continuation school where workers were encouraged to attend through a half-day off from work once a week either during the day or evening, to try and give the workers a chance at securing a better job.",
        "Waipahu, Hawaii, is roughly 10km west of Pearl Harbor and roughly 21km west of Honolulu.",
        "The name Waipahu translates to 'bursting water', and comes from the large body of water that rushes through the area."),

    "Avarua" : (
        "Avarua, which translates to 'Two Harbours' in Cook Islands Maori, is the capital city of the Cook Islands, located on the island Rarotonga, in the South Pacific Ocean.",
        "In December 1916, the commercial freighter SS Matai was transporting Model T cars when it ran aground of offshore reef near the town centre. Today, it is an attractive landmark for divers and snorkelers, and at low tides the engine can be seen from shore."),

    "Juneau" : (
        "Juneau is the capital city of Alaska and, (in terms of area) is the second largest city in the United States. The full name of the city is 'The City and Borough of Juneau' and comes from, back in 1970, voters electing to merge the city of Juneau with the city of Douglas and the surrounding Greater Juneau Borough",
        "Juneau, Alaska between the early 1930s - 1940s, was the home of Patsy Ann, a deaf white female English Pitt Terrier that frequented the wharfside. Despite being deaf, Patsy Ann was able to sense the arrival of ships, and the specific dock they were headed towards. Patsy's presence soon became a tourist attraction, and she was featured on several post cards. At one point, Patsy was sent to the pound due to a lack of a dog license, and in response the city bestowed Patsy the title of 'Official Greeter of Juneau, Alaska' in 1934. Patsy passed away in 1942, in her favourite spot: The Longshoreman's hall. She was sent off in a coffin lowered into the Gastineau Channel by a small crowd. Today she is remembered through a bronze sculpture that symbolically contains clippings of dog hair inside it, that continues to greet hundreds of ship the same way Patsy would have.",
        "On April 1 2016, Juneau, the capital city of Alaska, temporarily agreed to formally change their name to UNO, Alaska. This was a play-on-words, and a promotion by Mattel Inc. to draw attention to their new UNO cards, as well as to bring attention to the city as a potential tourist destination. When asked on his opinion, at the time 20 year old Michael Backus, coffee shop employee, was quoted as saying 'I like it.'"),

    "Sitka" : (
        "Sitka, Alaska is (as of the 2020 census) the 5th most populated city in Alaska, with a population of 8458 people, and (by area) the largest city in the United States. Between 1799 - 1867, the city was under Russian rule and was instead known as 'New Archangel'. The current name comes from a contraction of the Tinglit phrase 'Shee At ika' translating to 'People on the Outside of Baranof Island'.",
        "The 2009 romantic comedy 'The Proposal' starring Sandra Bullock as an editor-in-chief who pretends to be engaged to her assistant played by Ryan Reynolds features Sitka as the hometown of Ryan Reynolds. However, filming was primarily done in Rockport, MA instead.",
        "Russian explorers originally settled in what would become Sitka in 1799, naming it 'Fort of Archangel Michael'. In 1802 Tinglit warriors destroyed the settlement and forced the Russians out, who returned in 1804 with a ship that bombarded the settlement for two days until the Tinglist surrendered with a white flag. Back under Russian rule, the fort became known as 'New Archangel' and was the capital of Russia-America. Sitka wouldn't become an American city until 1867, when the United States purchased Alaska from the Russian Empire for USD 7.2 million (roughly USD 154 million in 2022)."),

    "Nome" : (
        "Nome, Alaska is a small city near the Bering Sea. It is estimated by the United States Census to house a population of 9865 people. It is however, perhaps best known for being the town in 1925 where a diphtheria epidemic occured, and due to blizzards the only method of delivering the antitoxin was via a relay of dog sled teams, one of which was led by the Siberian Husky: Balto!",
        "Nome, Alaska is a a remote community, covered in snow. In fact, it is so remote there are no roads connecting Nome to the rest of Alaska. The only way in or out of Nome is via air, boat or sled dog.",
        "Nome, Alaska hosts on of the world's largest gold pans, measuring approximately 20 feet in diameter. This is symbolic of Nome's economy, which heavily relies upon gold mining as a major source of employment and revenue today."),

    "Tijuana" : (
        "Tijuana, Mexico is (as of the 2020 census) the second most populated city in Mexico, with a population of over 2 million people! Located on the Pacific Coast of Mexico, the city's name comes from a ranch established in 1829 named 'Rancho Tia Juana', which was eventually shorthanded to 'Tijuana'. The origin of the original ranch name is disputed, suggested to be either from a derivation of the word 'Tiwan' meaning 'by the sea', in reference to an inn keeper known as 'Tia Juana' meaning 'Aunt Jane' in Spanish, or the word 'Tijuan' was derived from the name of a native Kumeyaay settlement nearby.",
        "Tijuana, Mexico's close location to San Diego, California means Tijuana is one of the only places in the world where a traveller (with their documents) can legally cross by foot from Mexico to the United States. Although the trip from San Diego to Tijuana is often quick, travellers are advised the trip from Tijuana to San Diego can include wait times of up to several hours. It is however, common for thousands of people to cross the border for a quick meal, doctor's appointment (otherwise known as Medical Tourism) or even to attend work/school!",
        "The Tijuana Cultural Center is home to the 'OMNIMAX', popularly dubbed as 'La Bola' (The Ball). It is a spherical IMAX theatre which utilizes a 360-degree projector to surround viewers with a panoramic image. For the first 13 years the threatre was opened, it showed a single movie, 'El Pueblo Del Sol' that showed representative images of Mexico. Today, the center offers a broad selection of films on a daily basis. The cultural centre also features an esplande, a museum and a separate theatre for live performances. The centre was originally designed for the purpose of promoting cultural tourism from the United States."),

    "Seattle" : (
        "Seattle is a seaport city and the largest city in the state Washington. Located roughly 100km north-east of the Washington capital Olympia, this famous city is home to the first ever Starbucks (opened in 1971), the first ever female mayor of a major American city (Bertha Ethel Knight Landes, elected in 1926-1928), the world's longest floating bridge (the Evergreen Point Floating Bridge), one of the world's first gas stations (opened in 1907), the city where America held its first ever strike (the Seattle General Strike in 1919), and the city where Grunge music first emerged in the mid-1980s",
        "Between 2011 to 2014, Seattle was home to the 'Rainy City Superhero Movement'. The organization, composed of their leader 'Phoenix Jones' (a professional mixed martial artist with a record of 7 wins, 1 draw and 3 losses), and members 'Buster Doe', 'Catastrophe', 'El Caballero', 'Gemini', 'Green Reaper', 'Karma', 'Midnight Jack', 'No Name', 'Penelope', 'Prodigy', 'Purple Reign', 'Red Dragon', 'SkyMan', 'The Mantis', 'Thorn', and 'Thunder 88' were a group of 'Real-life superheroes' that frequently performed nightly patrols. The group have notably stopped several instances of theft, assaults, have aided in the aprehension of sex offenders and have escorted people to their cars at night. Some cases have been uploaded onto Youtube under Phoenix Jones' account. The group was officially disbanded in 2014, and several members split off to create further real-life superhero teams such as 'ECHO' and 'Knightshift'.",
        "A global leader of culture and innovation, Seattle is home to a notably large LGBTQ+ community. The Seattle Times reported as of 2020, 10.7% of adults in Seattle identified themselves as being LGBTQ+. It is suggested to be the 6th largest LGBTQ+ population in the United States, and since 1974 has been home to the 'Seattle Pride', a series of events occuring in late June in Seattle celebrating LGBT Pride, and the weekly newspaper 'Seattle Gay News'."),

    "Vancouver" : (
        "Vancouver, Canada, is the largest city in Western Canada, boasting in 2021 652,248 people spread out over 5740 people per km^2, making it the also the city with the highest population density in Canada. The major city has been home to a number of global events, including the Commonwealth Games (1954), FIFA Women's World Cup (2015), Winter Olympics (2015), Winter Paralympics (2015), and since 2014, the permanent home of TED Conferences.",
        "Vancouver is ranked as one of the most ethnically diverse cities in Canada. Nearly half of all residents are non-native English speakers, and 54.5% of all residents belong to visible minority groups. When sorted by ethnic fractionalization (a range where a value of 1 suggests the population speaks 2 or more unrelated languages, and 0 = everybody speaks the same language), Canada was listed in 2003 as being 0.71, the 35th most diverse country in the world!",
        "Vancouver is home to Stanley Park, a 1001-acre public park that covers most of the northwestern side of Vancouver's downtown peninsula. It is approximately a 20% larger than New York City's Central Park. Notably, the park is home to the 9 O'Clock gun, a 680kg cast iron cannon now fired remotely precisely at 9pm originally designed used in 1894 for local fishermen to set their chronometers (a kind of clock) and warn them the fishing day was coming to an end. Prior to the cannon, Vancouver employed a stick of dynamite on a fishing rod instead! The cannon is empty and doesn't fire a cannonball every day. However, one prank in 1964 involved a child jamming a rock into the cannon, that when fired blased through the company sign on a refueling barage!"),

    "Denver" : (
        "Denver, Colorado is the capital and most populous city of Colorado. Located at the base of the Rocky Mountains, the city is surrounded by breaktaking natural beauty and is a popular destination for outdoor enthusiasts who enjoy hiking, surfing and other activities involving the mountains. It is known for the phrase '300 days of sunshine', that although is not necessarily true, suggests Denver sees 300 days of sunshine every year!",
        "Denver has a thriving microbrewery scene, with more than 200 breweries in the metro area. The city is known for its craft beer, and hosts a variety of beer festivals and events throughout the year, including the Great American Beer Festival and the Denver Beer Fest.",
        "Denver is known for its lively music and arts scene, and is home to many venues and festivals that showcase local and national talent. The city is also home to the Colorado Symphony Orchestra, which presents classical and contemporary music concerts throughout the year."),

    # This is where I burnt out
    "San_Luis_Rio_Colorado" : ("San Luis Río Colorado is a small city in Sonara, Mexico. Like many cities close to the United States-Mexico border, the city is a hotspot for people engaging in medical tourism and seeking affordable dental care.",
                               "San Luis Rio Colorado is located in the Sonoran Desert, which is known for its unique and diverse plant and animal life. Some species that can be found in the area include the saguaro cactus, desert tortoise, and jackrabbit."),

    "Sierra_Vista" : (
        "Sierra Vista is a city in southwestern Arizona, United States. In addition to scenic mountain views, it is home to Ramsey Canyon Preserve, a popular bird watching area home to over 150 bird species. It is open to hikes by visitors where they can also see a variety of different animals and plants.",
        "Sierra Vista is home to Fort Huachuca, which was established in 1877. The fort played an important role in the Indian Wars, and was also the site of the first airplane flight in Arizona. Fort Huachuca continues to serve as an important military installation, and is a major employer in the area."),

    "Chicago" : (
        "Chicago is a major sports city, with many professional teams and sports venues. The city is home to the Chicago Cubs and Chicago White Sox baseball teams, the Chicago Bears football team, and the Chicago Blackhawks hockey team, among others. Chicago is also a popular destination for major sporting events, including the Chicago Marathon and the annual NATO Summit.",
        "As a major city in the United States, it is unsurprising several TV shows were filmed in Chicago, such as: Chicago Fire, Empire, Shameless, Mindhunter, Easy, Good Trouble and Patriot.",
        "Chicago is home to an incredibly rich history, notable events including: The Great Chicago Fire of 1871, The Chicago Race Riot 1919 and The Chicago Seven Trial.",
        "Chicago is known for its food and restaurants. The city is famous for its deep-dish pizza, hot dogs, and other local specialties, and is also home to many world-class restaurants and chefs. Chicago is a popular destination for food lovers, and offers a diverse range of culinary options for residents and visitors alike."),

    "Quetzaltenango" : (
        "Also known by it's Mayan name 'Xela', Quetzaltenango is a city in Western Guatemala. It is the second-largest city in the country, after the capital, Guatemala City, and is known for its mild climate, beautiful scenery, and rich culture.",
        "The city of Quetzaltenango was founded in the 16th century, by the K'iche' people, who were one of the major civilizations of the ancient Maya. The city was originally called Xelajú, which means 'under the ten mountains' in the K'iche' language, and was an important center of trade and cultural exchange in the region.",
        "Quetzaltenango is located in the highlands of Guatemala, at an elevation of over 2,300 meters (7,500 feet) above sea level. The city is surrounded by beautiful scenery, including forests, mountains, and volcanoes. The city has a mild climate, which is cooler and more temperate than in other parts of Guatemala. This makes Quetzaltenango a great place to live for people who want to enjoy a comfortable climate year-round."),

    "Austin" : (
        "Austin is the capital city of Texas, and is the fourth-largest city in the United States. Located in the central part of Texas, Austin is known for its beautiful natural scenery, vibrant culture, and thriving economy. The city is home to many universities, including the University of Texas at Austin, and is a major center of education and research. Austin is also known for its music and arts scenes, and hosts many music festivals and other cultural events throughout the year. Austin is a diverse and vibrant city, with a rich history and many attractions for residents and visitors to enjoy.",
        "Austin is a major economic center in Texas, and is home to many businesses, factories, and other organizations. The city is known for its technology industry, and is home to many major tech companies, including Dell and IBM. Austin is also a popular destination for entrepreneurs and startups, and has a thriving entrepreneurial community. Furthermore, the city is situated along the Colorado River, and is surrounded by forests, hills, and lakes.",
        "The city of Austin was named after Stephen F. Austin, who was a pioneer and statesman in the early days of Texas. Stephen F. Austin was known as the 'Father of Texas,' and played a key role in the development and growth of the state. He was instrumental in helping to establish the Republic of Texas, and was a leader in the efforts to make Texas a part of the United States. In recognition of his contributions to the state, the city of Austin was named after him, and has become an important center of Texas history and culture."),

    "Philadelphia" : (
        "Philadelphia is the largest city in the state of Pennsylvania, and is one of the oldest and most historic cities in the United States. Located in the eastern part of the country, Philadelphia was founded in 1682, and played a crucial role in the early history of the United States. The city was the site of many important events during the American Revolution, including the signing of the Declaration of Independence in 1776. Philadelphia is known for its rich cultural and historical heritage, and is home to many museums, galleries, and other cultural institutions. The city is also a major center of education, healthcare, and business, and is home to many universities, hospitals, and companies.",
        "The TV show 'It's Always Sunny In Philadelphia' (IASIP) is shot in both Los Angeles and Philadelphia. As of its renewal for a 15th season in May 2020, IASIP is recognized as the American live-action show with the most seasons.",
        "Philadelphia cream cheese is not made in Philadelphia. The Philadelphia cream cheese brand is owned by the Kraft Heinz Company, which is based in Chicago. The cream cheese is made in a variety of locations around the United States, but not in Philadelphia. The name 'Philadelphia' was chosen for the brand because it was associated with quality and purity, and was seen as a trustworthy and reputable name. The brand has been very successful, and is now one of the most popular cream cheese brands in the world.",
        "The city of Philadelphia was named after the ancient Greek city of Philadelphia, which was located in the region of Lydia in modern-day Turkey. The ancient city of Philadelphia was named after King Attalus II Philadelphus, who was the ruler of the city in the second century BC. The name Philadelphia means 'brotherly love' in Greek, and was chosen to reflect the spirit of friendship and community that was seen as an important value in the city. The founders of the city of Philadelphia in the United States wanted to create a new community that was based on these same values, and chose the name Philadelphia to reflect this vision."),

    "Detroit" : (
        "Detroit is the largest city in the state of Michigan, and is located in the southeastern part of the United States. Detroit is known for its rich history and culture, and is a major center of industry and commerce. The city is home to many major companies, including General Motors and Ford Motor Company, and is a major hub of the automotive industry. Detroit is also a center of arts and culture, and is home to many museums, galleries, and other cultural institutions. The city has a diverse population and a vibrant economy, and offers many opportunities for residents and visitors to enjoy its rich history and culture.",
        "Detroit was once the world's leading producer of automobiles. In the early 20th century, Detroit was home to many major automotive companies, including General Motors, Ford Motor Company, and Chrysler. These companies helped to make Detroit the center of the automotive industry, and the city was known as the 'Motor City' for its many factories and assembly lines. Detroit was also a major center of innovation, and was home to many pioneering engineers and designers who helped to shape the modern automotive industry.",
        "Detroit is home to the Detroit River, a 32-mile-long river that flows through the city of Detroit and into Lake Erie. The river forms part of the border between the United States and Canada, and is an important waterway for commerce and transportation. The Detroit River is a major shipping channel, and is used by many large commercial vessels. The river is also a popular destination for recreational boating, fishing, and other outdoor activities. The Detroit River is known for its clean water and abundant wildlife, and is a vital part of the city's natural environment. The city has made significant efforts to protect and restore the river, and it is now considered one of the cleanest urban rivers in the United States."),

    "Lexington" : (
        "Lexington-Fayette is the name of a consolidated city-county in the state of Kentucky in the United States. The city of Lexington and the county of Fayette were merged into a single entity in 1974, and the city is now known as Lexington-Fayette. The city is the second-largest in Kentucky, and is the home of the University of Kentucky. Lexington-Fayette is known for its rich history and culture, and is a popular destination for tourists and visitors. The city is located in the heart of the Bluegrass region of Kentucky, and is known for its beautiful natural scenery and its many horse farms.",
        "The Cocaine Bear, also known as the Kentucky Bear, is a famous and bizarre incident that occurred in Lexington, Kentucky in 1985. The bear was discovered in the Daniel Boone National Forest, and was found to have ingested a large quantity of cocaine that had been smuggled into the area. The bear was later euthanized, and the incident became known as the Cocaine Bear. It is not clear how the bear came into contact with the cocaine, but the incident became a local legend and a source of fascination for many people. The Cocaine Bear is still remembered and discussed in Lexington today.",
        "Lexington is known as the 'Horse Capital of the World' because the city is home to many of the world's most famous and successful horse farms and equestrian events. The city is located in the heart of the Bluegrass region of Kentucky, which is known for its fertile soil and abundant grasses. These conditions are ideal for raising horses, and many of the world's most prestigious horse farms are located in and around Lexington. The city is also home to many equestrian events, including the famous Keeneland horse racing track and the Kentucky Horse Park. These factors have contributed to Lexington's reputation as the Horse Capital of the World."),

    "Caracas" : (
        "Caracas is the capital city of Venezuela, and is one of the largest cities in the country. The city is located in the northern part of Venezuela, and is situated in a valley at the foot of the Ávila mountain range. Caracas is known for its bustling metropolis, and is home to many museums, galleries, and other cultural attractions. The city is also a major center of industry and commerce, and is a hub of economic activity in the region. Despite its many advantages, Caracas has also faced challenges in recent years, including high levels of crime and political instability.",
        "Caracas is known for its lively nightlife, and is home to many bars, clubs, and restaurants. The city's vibrant nightlife scene offers something for everyone, and is a great place to experience the local culture and enjoy the city's many attractions. As a testament to the nightlife, Caracas is home to districts that are largely catered to the nightlife, including 'Las Mercedes', 'La Castellana', 'El Hatillo' and 'Chacaito'!"),

    "Mayaguez" : (
        "Mayagüez is a city on the western coast of Puerto Rico, and is the third-largest city on the island. The city is located in the western part of the island, near the border with the Dominican Republic, and is a major center of trade and commerce. Mayagüez is known for its vibrant culture and history, and is home to many museums, galleries, and other cultural attractions. The city is also a hub of economic activity, and is home to many businesses and industries. Despite its many advantages, Mayagüez has also faced challenges in recent years, including high levels of crime and economic instability.",
        "Mayagüez is the birthplace of Puerto Rico's flag. The flag was designed by Dr. Ramón Emeterio Betances, a Puerto Rican independence activist, and was first flown in the city on March 24, 1892. The flag, which consists of five alternating red and white stripes, has since become an important symbol of Puerto Rico's national identity.",
        "Mayagüez was the first city in Puerto Rico to have a public library. The library was founded in 1853, and was named the 'Biblioteca Pública de Mayagüez' (Mayagüez Public Library). The library, which is still in operation today, is located in the city's historic center, and is a popular destination for book lovers and those interested in the city's cultural heritage."),

    "Riberalta" : (
        "Riberalta is a city in the Beni department of Bolivia. The city is located in the Amazon rainforest, and is the capital of the province of Riberalta. Riberalta is an important economic and transportation hub for the region, and is a major center of trade and commerce. The city is also a popular destination for tourists, who come to experience the region's unique natural beauty and biodiversity. Some of the main attractions in and around Riberalta include the Madidi National Park, the Beni River, and the Capitania river port.",
        "Riberalta is located in the Amazon rainforest, which is one of the most biodiverse regions on the planet. The city is surrounded by a vast expanse of tropical forests, which are home to an incredible variety of plants and animals. The region is particularly known for its rich bird life, and is a popular destination for birdwatchers from around the world. The Madidi National Park, located just outside of Riberalta, is a protected area that is home to many endangered species, including the jaguar, the giant otter, and the Andean condor.",
        "Another interesting fact about Riberalta is that it is home to a diverse and multicultural population. The city has a rich history of immigration, and has been influenced by many different cultures and traditions. The population of Riberalta includes people of indigenous, African, European, and Asian descent, and is a melting pot of different cultures and languages. The city is also home to many different religious communities, including Christians, Muslims, and followers of traditional indigenous religions. This diversity is reflected in the city's art, music, and cuisine, which are a blend of different influences and traditions. Riberalta is a city that is proud of its multicultural heritage, and continues to celebrate its diversity and inclusivity."),

    "Buenos_Aires" : (
        "Buenos Aires is known for its rich and diverse cultural heritage. The city has a long history of immigration, and has been influenced by many different cultures and traditions. This diversity is reflected in the city's art, music, and cuisine, which are a blend of different influences and traditions. Buenos Aires is home to many museums, galleries, and theaters, and is a major center of cultural activity in South America. The city is also known for its vibrant nightlife scene, and is home to many bars, clubs, and restaurants.",
        "Buenos Aires is home to many historic and architectural landmarks, which are a testament to the city's rich history and culture. The city's historic center, known as San Telmo, is home to many colonial-era buildings and cobbled streets, and is a popular destination for tourists. The city's other neighborhoods also have their own unique architectural styles, and are home to many beautiful and historic buildings. Some of the most famous landmarks in Buenos Aires include the Casa Rosada, the Obelisco, and the Teatro Colón.",
        "Buenos Aires is interestingly home to one of the world's largest Chinatowns. The neighborhood, known as Barrio Chino, is located in the city's Belgrano district, and is home to many businesses and restaurants that cater to the city's Chinese community. The neighborhood, which was established in the early 20th century, is known for its vibrant and lively atmosphere, and is a popular destination for tourists and locals alike. The neighborhood is also home to many cultural and community organizations, and hosts many festivals and events throughout the year. Buenos Aires' Chinatown is a unique and fascinating part of the city, and is a must-see destination for anyone interested in the city's multicultural heritage."),

    "Rio_de_Janeiro" : (
        "Rio de Janeiro is home to many cultural and historical landmarks, which are a testament to the city's rich heritage. The city's historic center, known as the Centro, is home to many colonial-era buildings and cobbled streets, and is a popular destination for tourists. The city's other neighborhoods also have their own unique architectural styles, and are home to many beautiful and historic buildings. Some of the most famous landmarks in Rio de Janeiro include the Christ the Redeemer statue, the Sugarloaf Mountain, and the Maracanã Stadium.",
        "Rio de Janeiro is known for its vibrant and colorful culture, which is a blend of many different influences and traditions. The city is home to many different communities and ethnic groups, and is a melting pot of different cultures and languages. This diversity is reflected in the city's art, music, and cuisine, which are a blend of different influences and traditions. Rio de Janeiro is also known for its lively nightlife scene, and is home to many bars, clubs, and restaurants.",
        "Rio de Janeiro has a long and rich history, dating back to the early 16th century. The city was founded by the Portuguese in 1565, and was initially called São Sebastião do Rio de Janeiro. The city quickly became an important center of trade and commerce, and was an important port for the Portuguese empire. Rio de Janeiro was also an important center of culture and art, and was home to many writers, artists, and intellectuals. During the 18th and 19th centuries, Rio de Janeiro was the capital of Brazil, and was a major center of political and cultural activity. The city was also an important center of the slave trade, and was home to many African slaves and their descendants. In the late 19th and early 20th centuries, Rio de Janeiro underwent rapid industrialization and urbanization, and became one of the largest and most populous cities in South America."),

    "Vitoria_da_Conquista" : (
        "Vitória da Conquista's art scene is vibrant and diverse, and is home to many galleries and museums. The city's art is influenced by its rich history and culture, and is a reflection of the city's many different communities and traditions. The city's music is also diverse, and is influenced by many different genres and styles, including Afro-Brazilian, Indigenous, and European music. The city's cuisine is also a reflection of its diverse culture, and is a blend of different flavors and ingredients.",
        "The city of Vitória da Conquista was originally named São Francisco de Sales, but was renamed in the mid-19th century, after the victory of the Brazilian army over the Paraguayan army in the War of the Triple Alliance. The new name, Vitória da Conquista, means 'Victory of the Conquest' in Portuguese, and was chosen to commemorate the Brazilian victory in the war. The new name was chosen to reflect the city's growing importance and strategic location, and was intended to help the city attract new residents and businesses."),

    "Fernando" : (
        "Fernando de Noronha is a small Brazilian archipelago located in the Atlantic Ocean, about 354 kilometers off the coast of Brazil. The archipelago consists of 21 islands, of which the largest is also called Fernando de Noronha, and is also home to many unique and endangered species of plants and animals such as sea turtles, dolphins and birds. The archipelago is a UNESCO World Heritage Site, and is known for its beautiful beaches, crystal clear waters, and rich marine life.",
        "Fernando de Noronha was first discovered by the Portuguese explorer Américo Vespúcio in 1503. The islands were named after the Portuguese nobleman Fernando de Noronha, who was an important figure in the Portuguese court. The islands were used as a base for the Portuguese navy, and were also a center of commerce and trade.",
        "Fernando de Noronha is a popular destination for scuba diving and other water sports, due to the clear waters and rich marine life. The waters around the islands are home to many different species of fish, coral, and other marine life, and are a popular destination for divers and other water enthusiasts."),

    "Praia" : (
        "Praia is located on the southern coast of the island of Santiago, and is surrounded by beautiful beaches and crystal clear waters. These beaches are popular destinations for swimming, sunbathing, and other water sports, and are an important part of the city's economy and culture.",
        "Praia was founded in the 16th century by the Portuguese, who used the city as a base for their trade and commerce activities in the region. Over the centuries, Praia has grown into a major city, and is now home to a diverse population of people from many different backgrounds and cultures.",
        "Praia is the oldest city in Cape Verde, and was founded by the Portuguese in the 16th century. The city was originally called Ribeira Grande, and was a major hub of trade and commerce in the region. Over the centuries, Praia has grown and developed into a modern city, and is now the commercial, cultural, and political center of Cape Verde."),

    "Flores_Island" : (
        "Flores Island is an island in the Azores archipelago, located in the North Atlantic Ocean. The island is known for its beautiful landscapes, which are characterized by rolling hills, verdant forests, and stunning coastal views. The island is home to many scenic hiking trails, which offer breathtaking views of the surrounding landscapes, as well as opportunities to explore the island's natural beauty. One of the most beautiful landscapes on the island is the Lagoa do Fogo, a crater lake located in the island's interior. The lake is surrounded by lush forests and verdant hills, and is a popular destination for hikers and nature lovers. Another popular spot on the island is the Miradouro da Fajãzinha, a viewpoint overlooking the ocean, which offers stunning views of the coast and the surrounding landscape.",
        "Flores Island was founded by the Portuguese in the 15th century. The island was first discovered by the Portuguese explorer Diogo de Silves in 1452, and was later colonized by the Portuguese in the early 1500s. The island was named Flores, which means 'flowers' in Portuguese, due to the abundance of wildflowers that grew on the island.",
        "Flores Island makes a brilliant tourist destination due to its beautiful landscapes. The island is home to many scenic hiking trails, which offer breathtaking views of the surrounding landscapes, as well as opportunities to explore the island's natural beauty. The island is also home to many beautiful beaches and coastal areas, which are popular destinations for swimming, sunbathing, and other water activities. In addition to its beautiful landscapes, Flores Island is also home to many interesting historical and cultural attractions. The island is home to many museums, galleries, and other cultural attractions, which offer visitors a glimpse into the island's rich history and vibrant culture. The island is also home to many historic buildings and landmarks, including the 16th century Church of Santa Cruz and the 17th century Fort of São João Baptista."),

    "London" : (
        "London is a major cultural and artistic center, and is home to many famous writers, artists, and musicians. Some of the most notable writers who have lived and worked in London include: William Shakespeare, bane of all 16 year old English students, J.K. Rowling, who wrote the bestselling Harry Potter series, Charles Dickens, who may be more commonly known for writing 'A Christmas Carol' and 'Oliver Twist' and Oscar Wilde who you may have heard of as the author of works such as 'The Picture of Dorian Gray' or 'The Importance of Being Earnest'",
        "London has a long history of brewing and distilling, and has been home to many famous breweries and distilleries over the years. Some of the most well-known London breweries include the Fuller's Brewery, the Meantime Brewery, and the Camden Town Brewery. London has also been home to many famous pubs and taverns, which have been important social and cultural centers for the city's residents. Some of the most famous pubs in London include the Olde Cheshire Cheese, the White Hart, and the Ye Olde Mitre. In addition to its breweries and pubs, London has also been home to many famous bars and nightclubs, which have played a significant role in the city's nightlife and entertainment scene. Some of the most well-known bars and nightclubs in London include the Roxy, the Fabric, and the Ministry of Sound.",
        "London is home to the world's oldest underground railway system. The London Underground, also known as the 'Tube', was first opened in 1863, and has been in continuous operation ever since. It is the world's first and oldest underground railway network, and is an important part of London's public transportation system. The London Underground is one of the busiest railway networks in the world, and carries over 1.3 billion passengers every year. It is made up of 11 lines, and has over 250 stations. The network covers a total distance of 402 kilometers, and serves a large area of London and the surrounding suburbs. The London Underground is an important part of London's history and culture, and is a popular tourist attraction in its own right. Many visitors to London enjoy taking a ride on the 'Tube' to experience the city's unique and fascinating underground railway system."),

    "Dublin" : (
        "Dublin is the capital city of Ireland, and is located on the east coast of the country. It is one of the oldest cities in Europe, and has a rich and fascinating history.The city was founded by the Vikings in the 9th century, and was later settled by the Normans. Dublin has been an important center of trade, commerce, and culture for many centuries, and has played a significant role in the history of Ireland. Today, Dublin is a vibrant and cosmopolitan city, with a population of over 1 million people. The city is a major center of education, culture, and economic activity, and is home to many world-class institutions and attractions.",
        "Dublin was once home to a giant wooden horse. The horse was built in the 19th century, and was intended to be a tourist attraction. However, the horse was too big to be moved, and was eventually abandoned. The wooden horse was located in Dublin's Phoenix Park, and was intended to be a replica of the Trojan Horse from Greek mythology. The horse was built by a local carpenter, and was over 100 feet tall. However, the horse was never completed, and was eventually abandoned. It remained in Phoenix Park for many years, until it was eventually demolished in the 1930s. Today, the site of the wooden horse is a popular tourist attraction, and is often visited by visitors to Dublin. Despite its failure as a tourist attraction, the wooden horse remains an interesting and amusing part of Dublin's history.",
        "Dublin is often referred to as the 'literary capital of the world', and is the birthplace of many famous writers, including James Joyce, Oscar Wilde, and Samuel Beckett. The city is home to many literary institutions, including the Dublin Writers Museum, the James Joyce Centre, and the Dublin Literary Pub Crawl.",
        "Dublin was once home to a giant wooden statue of King Billy. The statue was built in the 19th century, and was intended to be a tribute to King William III of England, who was also known as King Billy. The statue was located in Dublin's College Green, and was over 30 feet tall. It was built by a local sculptor, and was made of wood and plaster. However, the statue was not well-received by the people of Dublin, and was frequently the subject of ridicule and satire. Many people thought the statue was ugly, and it was often the target of vandalism and graffiti. In the end, the statue was removed and demolished, and today it is largely forgotten."),

    "Grenoble" : (
        "Grenoble is home to several research institutes and universities, making it an important center of scientific and technological innovation. The city is known for its research in fields such as electronics, renewable energy, and biotechnology. Amongst several incredible scientists, Grenoble is also home to computer scientist Guillaume Cabanac, who in 2021 was named as one of Nature's top 10 scientists of the year for his work with his colleague Cyril Labbé in identifying cases of computer-generated science articles that spouted nonsensical rubbish such as: the use of the phrase 'Bosom Malignancy' to describe Breast Cancer!",
        "Grenoble is a city in southeastern France, located in the Auvergne-Rhône-Alpes region. It's the largest city in the region and the capital of the Isère department. Grenoble is known for its natural beauty, with the French Alps and the Vercors Massif nearby. The city has a rich history and culture, and it's home to several universities and research institutes. It's also a popular tourist destination, known for its museums, galleries, and outdoor activities.",
        "Grenoble is a city with a long history that dates back to ancient times. It was founded by the Gauls in the 4th century BC and later became a Roman settlement. The city's name is derived from the Gaulish word 'Granniobles' which means 'town of the council' Over the centuries, Grenoble has been an important center of trade, culture, and political power, with a rich and diverse history that has shaped its culture and identity. Throughout its history, Grenoble has been a strategic location for trade and transportation, due to its position at the confluence of the Drac and Isère rivers. The city was an important center of trade and commerce during the Middle Ages, and it later became a key hub of the French railroad network. In the 19th and 20th centuries, Grenoble grew into a major industrial city, with a focus on heavy industry and manufacturing. Grenoble has played a significant role in French history, particularly during the French Revolution. The city was the site of several important political events, including the overthrow of the local monarchy and the establishment of the first French Republic.",
        "Grenoble is located at the foot of the French Alps, which makes it a popular destination for outdoor activities such as hiking, skiing, and mountain biking. The city is also home to the world's largest urban cable car network, which provides access to the nearby mountains and offers stunning views of the surrounding area. The city's location at the base of the Alps gives it a unique natural setting that attracts visitors from around the world. The nearby mountains offer a wide range of outdoor activities, from skiing and snowboarding in the winter to hiking and mountain biking in the summer. The city is also home to several nature reserves and protected areas, including the Vercors Massif, which offers beautiful landscapes and a rich variety of flora and fauna. Grenoble's urban cable car network is another unique feature of the city. The network consists of several cable cars that provide access to the nearby mountains, offering stunning views of the surrounding area. The cable cars are a popular attraction for visitors and locals alike, and they are an important part of the city's transportation network, providing an eco-friendly alternative to cars and buses."),

    "Vienna" : (
        "Vienna has a rich and diverse cultural heritage, with a long history as a center of art and music. The city was the home of many famous composers, including Wolfgang Amadeus Mozart, Ludwig van Beethoven, and Johann Strauss II. Vienna is also known for its architectural treasures, including the Baroque-style Schönbrunn Palace and the Gothic St. Stephen's Cathedral. Vienna's cultural heritage is also celebrated through many annual events and festivals, such as the Vienna Festival and the Wiener Festwochen, which showcase a wide range of performances and exhibitions.",
        "As the seat of the United Nations, Vienna is an important hub for international diplomacy and cooperation. Many important international meetings and conferences are held in the city, which serves as a neutral and convenient location for international negotiations. The UN headquarters in Vienna is one of four UN headquarters around the world, and it's home to several key UN agencies, including the International Atomic Energy Agency (IAEA) and the United Nations Industrial Development Organization (UNIDO)."),

    "Athens" : (
        "Athens is one of the oldest cities in Europe, with a history that spans more than 3,000 years. The city was the birthplace of Western civilization, and it has played a crucial role in the development of art, science, and philosophy. The city's rich history is reflected in its many historical and cultural landmarks, such as the Parthenon and the Acropolis. The city of Athens was founded in the 9th century BC, and it soon became a major center of trade and commerce. In the 5th century BC, Athens became the capital of the powerful city-state of Attica, and it was the center of the Greek world. During this period, Athens was known for its cultural and artistic achievements, and it was home to many famous philosophers, artists, and scientists, such as Socrates, Plato, and Aristotle.",
        "Athens is home to the National Archaeological Museum, which houses one of the world's largest collections of ancient Greek artifacts, and the National Library of Greece, which is one of the country's most important cultural institutions. The city's cultural scene is vibrant and diverse, with many museums, galleries, and theaters that showcase a wide range of art, music, and performances. The National Archaeological Museum is one of the city's most popular cultural attractions, and it houses a vast collection of artifacts from ancient Greece, including sculptures, pottery, and jewelry. The National Library of Greece is another important cultural institution, and it's home to more than 4 million books and manuscripts, including many rare and valuable works.",
        "Athens is home to many breweries and brewpubs, which produce a wide range of beers, from lagers and pilsners to ales and stouts. Many of these beers are made with local ingredients, such as barley, hops, and water from the region, and they are popular with locals and tourists alike. Some of the most famous beers from Athens include Mythos, Alpha, and Fix. In addition, the Attica region in Athens is home to many vineyards and wineries, and it produces a variety of wines, including red, white, and rosé wines. The region's wines are made with grapes that are grown in the local vineyards, and they are known for their high quality and distinctive flavors. Some of the most famous wines from the Attica region include Agiorgitiko, Savatiano, and Moschofilero."),

    "Kiev" : (
        "Kiev has a tradition of brewing beer, and there are many breweries and brewpubs in Kiev that produce a wide range of beers, from lagers and pilsners to ales and stouts. The city's beer culture dates back to the 9th century, when Kiev was the center of the powerful Kievan Rus' state. The city was a major hub of trade and commerce, and beer was an important part of the local economy and culture. The city's brewers used local ingredients, such as barley, hops, and water from the region, to produce high-quality beers that were popular with locals and traders. Today, the city's beer culture is still thriving, and there are many breweries and brewpubs in Kiev that produce a wide range of beers. These breweries use modern technology and techniques to produce high-quality beers, and they are popular with locals and tourists alike. Many of the city's breweries and brewpubs also offer tours and tastings, where visitors can learn more about the history of beer in Kiev and sample some of the city's delicious brews.",
        "Kiev has a vibrant arts and culture scene, with many museums, galleries, and theaters. The city is home to many cultural institutions, such as the Kiev Opera, the National Museum of Ukrainian History, and the National Art Museum of Ukraine. These institutions host a variety of exhibitions, performances, and events, and they are an important part of the city's cultural life.",
        "Kiev is one of the oldest cities in Eastern Europe, and it has a rich and diverse history that spans more than 1,500 years. The city was founded in the 5th century AD, and it has been an important center of trade, commerce, and culture throughout its history. The city was founded in the 5th century AD by Slavic tribes who settled in the area. The city was located at the intersection of important trade routes, and it quickly became a major center of commerce and trade. In the 9th century, Kiev was the center of the powerful Kievan Rus' state, which was a major political, economic, and cultural force in Eastern Europe. The city was the birthplace of the Slavic civilization, and it was a key hub of trade and commerce, connecting the East and the West."),

    "Suez" : (
        "In ancient times, Suez was a major center of the beer and alcohol trade, and it was a key port of entry for these products from the lands of the East. The city was located on the Red Sea, which was an important trade route, and it was a major center of the trans-Saharan trade in beer and alcohol. The city's brewers used local ingredients, such as barley and hops, to produce high-quality beers and spirits that were popular with locals and traders. During the medieval period, Suez continued to be an important center of the beer and alcohol trade, and it was a key transit point for these products between the Mediterranean and the Indian Ocean. The city's brewers continued to produce high-quality beers and spirits, and they were known for their delicious and unique flavors. Many of the city's beers and spirits were exported to other parts of the world, and they were highly regarded for their quality and taste. Today, Suez is still an important center of the beer and alcohol industry, and it's home to many breweries and distilleries that produce a wide range of products. These breweries use modern technology and techniques to produce high-quality beers and spirits, and they are popular with locals and tourists alike. Many of the city's breweries and distilleries also offer tours and tastings, where visitors can learn more about the history of beer and alcohol in Suez and sample some of the city's delicious brews.",
        "One of the things that makes Suez so interesting is its diversity of cultures and traditions. The city has a long history of being a center of trade and commerce, and it has been influenced by many different cultures over the years. As a result, the city has a unique blend of cultures and traditions, and it's a fascinating place to explore. One of the things that you'll notice when you visit Suez is the diversity of its architecture. The city has a mix of old and modern buildings, and you'll see a range of architectural styles, from ancient ruins to modern skyscrapers. The city is also home to many historical and cultural landmarks, such as the Suez Canal, the Suez Museum, and the Suez Citadel. These landmarks are popular tourist destinations, and they provide a fascinating glimpse into the city's rich history and culture.",
        "The Suez Canal is a man-made waterway that connects the Mediterranean Sea and the Red Sea, and it's a major transit route for ships and cargo between Europe and Asia. The construction of the canal was a major engineering feat, and it was completed in 1869. The idea of building a canal to connect the Mediterranean and the Red Sea was first proposed by the ancient Egyptians, and they attempted to build such a canal several times throughout their history. However, these efforts were unsuccessful, and the idea of a canal was not seriously pursued until the 19th century. The Canal was an engineering marvel, and it was one of the largest and most ambitious construction projects of its time. The canal was built using manual labor and simple tools, and it was an incredible feat of engineering and human ingenuity. In 2021, the Canal was famously blocked by a container ship running aground, disrupting global trade for seven days."),

    "Istabnul" : (
        "Istanbul has a long and rich history of brewing and consuming beer and alcohol, and the city has been an important center of the beer and alcohol trade for many centuries. The city's brewers have been producing high-quality beers and spirits for hundreds of years, and these products are an important part of the city's culture and economy. The city is famous for its unique and delicious beers and spirits, and many of the city's products are known for their distinct flavors and aromas. Some of the city's most popular beers and spirits include raki, a spirit made from aniseed, and Efes, a popular brand of beer. These products are an important part of Istanbul's culture, and they are enjoyed by locals and visitors alike.",
        "Cats have been a part of Istanbul's history and culture for many centuries, and they have been associated with the city for a long time. In ancient times, cats were worshipped by the Egyptians, and they were considered to be sacred animals. When the Ottoman Empire was founded, cats were introduced to Istanbul, and they quickly became a common sight in the city. The city's authorities and local residents are committed to ensuring that the cats of Istanbul are healthy and happy, and they work together to provide the cats with the care and support that they need. There are several videos of cats lying on top of counters in convenience stores.",
        "The city of Istanbul is located in two different continents: Europe and Asia. The city is divided by the Bosphorus Strait, which separates Europe and Asia, and it's the only city in the world that is located on two different continents. Tourists can take a boat tour along the strait. You can take a boat tour on the Bosphorus and enjoy the beautiful scenery and views of the city. The boat tour is a great way to experience the beauty and charm of Istanbul, and it's an activity that is suitable for all ages."),

    "Ryazan" : (
        "Ryazan is a city located in central Russia, and it's the administrative center of Ryazan Oblast. The city is located on the Oka River, and it has a population of around 540,000 people.",
        "Ryazan was founded in the 10th century, and it played an important role in Russian history. The city was a center of trade and commerce, and it was an important stop on the trade route between Moscow and the Black Sea. Ryazan was also an important center of the arts and culture, and it was home to many writers, artists, and musicians."),

    "Dubai" : (
        "Dubai has a strict and conservative attitude towards alcohol, and the consumption, sale, and distribution of alcohol are tightly regulated. In Dubai, alcohol can only be consumed in licensed premises, such as bars, clubs, and hotels, and it's illegal to drink alcohol in public. Tourists who want to drink alcohol in Dubai must obtain a special license, which can be obtained from the Dubai Department of Tourism and Commerce Marketing. Despite the restrictions on alcohol, Dubai has a thriving and vibrant nightlife, and there are many places where tourists can enjoy a drink. The city is home to many bars, clubs, and restaurants that serve alcohol, and these venues are popular with tourists and locals alike. The city also has many hotels that have bars and lounges where tourists can enjoy a drink, and these venues are often a great place to relax and unwind after a day of sightseeing.",
        "Dubai is home to many breweries and distilleries that produce a wide range of beers and spirits. The city's brewers use local ingredients, such as barley and hops, to produce high-quality beers and spirits that are popular with locals and tourists alike. Many of the city's breweries and distilleries also offer tours and tastings, where visitors can learn more about the history of beer and alcohol in Dubai and sample some of the city's delicious brews.",
        "Dubai is home to the world's tallest building, the Burj Khalifa. The Burj Khalifa is an iconic and imposing skyscraper, and it stands at a staggering height of 828 meters (2,722 feet). The building was completed in 2010, and it has been the tallest building in the world ever since. The Burj Khalifa is an engineering marvel, and it's a must-see attraction for tourists in Dubai.",
        "Dubai is a city that is known for its opulent and luxurious lifestyle, and it's a place where you can find some of the most expensive and exclusive hotels and resorts in the world. The city is home to many luxury hotels and resorts, and they offer a wide range of amenities and services that are designed to cater to the needs and desires of the most discerning guests. The city's hotels and resorts are famous for their opulence and luxury, and they are a great place to relax and unwind in style."),

    "Qazax" : (
        "Qazax is a city located in Azerbaijan, and it's the administrative center of the Qazax District. The city is located in the northeast of the country, and it has a population of around 60,000 people. Qazax is an important industrial and economic center, and it's a major hub for the region's agriculture and industry.",
        "The history of beer and alcohol in Qazax dates back to ancient times, and the city has a long and storied tradition of brewing and distilling. The city's brewers and distillers have used local ingredients, such as barley and hops, to produce a wide range of beers and spirits. The city's brewers and distillers were known for their skill and expertise, and they were renowned for their delicious and high-quality brews. Despite the city's rich and storied tradition of brewing and distilling, the consumption, sale, and distribution of alcohol in Qazax are tightly regulated. In Qazax, alcohol can only be consumed in licensed premises, such as bars, clubs, and hotels, and it's illegal to drink alcohol in public. Tourists who want to drink alcohol in Qazax must obtain a special license, which can be obtained from the Qazax District Administration.",
        "Qazax is home to the world's largest mausoleum, and it's a must-see attraction for tourists in the city. The mausoleum is located in the city's central square, and it's a huge and imposing structure that stands at a staggering height of 30 meters (98 feet). The mausoleum was built in the 19th century to honor the city's founder, and it's a popular attraction for tourists and locals alike. The mausoleum is a great place to learn more about the city's history and culture, and it's a must-see attraction for anyone visiting Qazax."),

    "Oral" : ("The city of Oral was named after the river Ural, which flows through the city. The river Ural is a major waterway that flows through the region, and it's an important transportation and trade route. The river was named after the Ural Mountains, which are a major mountain range that extends across much of northern and central Eurasia.",
              "Oral is home to the Oral History Museum, which displays artifacts and exhibits related to the city's history and culture. The museum is located in a 19th-century merchant's house and is considered one of the best museums in Kazakhstan."),

    "Karachi" : ("Karachi is the largest city in Pakistan, and it's the country's financial and economic hub. The city is located on the coast of the Arabian Sea, and it has a population of around 14.9 million people.",
                 "Karachi is located on the Arabian Sea, which makes it an important port city and transportation hub in Pakistan. The city is home to the Karachi Port, which is the largest and busiest port in the country and handles a significant amount of trade and commerce. This makes Karachi an easy place to travel to and from, as it is well-connected by air, road, and sea."),

    "Dhaka" : ("Dhaka, also known as Dacca, is the capital city of Bangladesh and one of the largest cities in South Asia.",
               "Dhaka is located in the heart of Bangladesh, which makes it an important transportation hub in the country. The city is home to the Hazrat Shahjalal International Airport, which is the busiest airport in Bangladesh and serves as a hub for several major airlines. In addition to air travel, Dhaka is also well-connected by road and rail, with a number of major highways and railway lines passing through the city. This makes it easy to travel to and from Dhaka, and to other destinations in Bangladesh and the surrounding region."),

    "Mirny" : ("Mirny Station is a Russian research station in Antarctica. It was established in 1957 and is currently operated by the Russian Antarctic Expedition. The station is located on the shore of Lake Vostok, one of the largest subglacial lakes in Antarctica, and is used as a base for scientific research in the surrounding area. The station has a maximum capacity of around 50 people and is equipped with living quarters, laboratories, and other facilities for conducting research.",
               "Mirny Station is a Russian research station in Antarctica. It was established in 1957 and is currently operated by the Russian Antarctic Expedition. The station is located on the shore of Lake Vostok, one of the largest subglacial lakes in Antarctica, and is used as a base for scientific research in the surrounding area. The station has a maximum capacity of around 50 people and is equipped with living quarters, laboratories, and other facilities for conducting research."),

    "Jakarta" : (
        "Jakarta is home to a diverse range of religious communities, including Muslims, Christians, Buddhists, and Hindus. Islam is the dominant religion in Jakarta, with a majority of the city's population identifying as Muslim. The city is home to a number of important Islamic landmarks and institutions, including the Istiqlal Mosque, the largest mosque in Indonesia, and the Jakarta Islamic Center, which is a major center for Islamic study and worship. However, Indonesia, a predominantly Muslim country, is also home to a number of other religions, and the government promotes religious tolerance and diversity. This cultural diversity is reflected in the makeup of Jakarta's population, which includes people of different religious backgrounds living and working together in harmony.",
        "Jakarta is home to the National Monument (in Indonesian known as 'Monumen Nasional', abbreviated as Monas) a 132-meter-tall tower located in the center of Jakarta, Indonesia. It was built to commemorate the Indonesian struggle for independence and is a symbol of the sacrifices and struggles of the Indonesian people during their fight for independence from Dutch colonial rule. It is now a popular tourist attraction and a symbol of Indonesian nationalism. The tower is made of bronze and is shaped like a flame, which is a symbol of the struggles and sacrifices of the Indonesian people. The base of the tower is surrounded by a park, which is a popular place for locals to relax and spend time with their families. The observation deck at the top of the tower offers panoramic views of Jakarta, and there is also a museum inside the tower that showcases the history of Indonesia's independence movement.",
        "Jakarta is the capital and largest city of Indonesia, and the official language of Jakarta is Indonesian, which is the national language of Indonesia. However, many people in Jakarta also speak other languages, including English and Chinese, as well as Dutch, which was once the official language of Indonesia during the colonial period. Both Chinese and English are also widely spoken in Jakarta, English in particular spoken among the business community. Many schools in Jakarta teach English as a second language, and it is often used as a common language for communication between people of different linguistic backgrounds."),

    "Bangkok" : (
        "Bangkok is the capital and largest city of Thailand, and it is known as the 'City of Angels' in Thai. The city is located on the eastern bank of the Chao Phraya River, and it is the most populous city in Thailand, with a population of over 8 million people. Bangkok is a major cultural, economic, and political center in Southeast Asia, and it is a hub for tourism, with over 20 million visitors each year. The city is known for its vibrant street life, delicious food, and ornate temples, and it is home to a number of interesting museums and cultural attractions. Despite its modernity and cosmopolitan atmosphere, Bangkok is also home to a number of traditional neighborhoods, such as the old town of Rattanakosin, which is home to many of the city's most famous temples and landmarks. The city is known for its hot and humid climate, with an average temperature of around 30 degrees Celsius (86 degrees Fahrenheit) year-round.",
        "Bangkok is known as the 'City of Angels' in Thai because its full name is, 'Krung Thep Maha Nakhon'. The name 'Krung Thep Maha Nakhon' is often shortened to 'Krung Thep' for brevity, and this name is sometimes translated as 'The City of Angels'. This name is a reference to the many temples and palaces in the city that were once home to the gods and the royal family.",
        "Bangkok is home to a number of malls selling luxury international brands such as Chanel, Louis Vuitton, Gucci, and some local luxury brands like Sretsis, Issara and Roda. Bangkok is home to a number of wealthy individuals and families, who have a strong purchasing power and are willing to spend money on luxury brands. This, in combination with the fact that Bangkok is a major tourist destination, with over 20 million visitors each year, many of which are attracted to the city's shopping and are willing to buy luxury brands as souvenirs or gifts, make Bangkok an attractive city for luxury brands to sell their goods. "),

    "Shanghai" : (
        "Shanghai hosts the aptly named Shanghai Tower, a skyscraper recognized as the second tallest building in the world, with a height of approximately 632 metres. The Shanghai Tower was designed by the American architectural firm Gensler, and was completed in 2015. It is a mixed-use building, and contains offices, hotel rooms, and retail space. The building has 121 floors, and features a unique design that tapers towards the top, with a spiral shape that twists as it rises. The tower is an iconic symbol of the city, and offers tourists panormaic views of the city on the observation deck located on the 118th floor.",
        "Shanghai is home to the world's first and largest operational magnetic levitation (maglev) train line. The Shanghai Maglev Train runs from the city center to Pudong International Airport, and can reach speeds of up to 430 km/h.",
        "Shanghai is home to the largest Starbucks store in the world, located in the Shanghai Tower, opened in 2017. The store occupies nearly 2800 square metres and has seating for over 1000 customers. It is a multi-story store, and includes a spiral staircase and a two-story, glass-enclosed coffee roastery. The store also includes a Teavana tea bar, a Princi bakery and a wall full of Chinese calligraphy."),

    "Manila" : (
        "Manila is home to the world's oldest Chinatown, which dates back to the 1594. The district is called Binondo, and is also home to a number of historical landmarks, including the Binondo Church, which is a Spanish colonial-era church that was built in the 1596, and the Chinatown Heritage Center, which is a museum that documents the history of the Chinese community in the Philippines.",
        "Manila is a vibrant and culturally diverse city, and is home to a number of festivals and events throughout the year. These events celebrate the city's rich culture and history, and offer visitors a chance to experience a wide range of activities and attractions. Events include the Manila Pride Parade, the Feast of the Black Nazarene, the Philippine Intewrnational Hot Air Balloon Festival, The Manila Food and Wine Festival and the Manila Film Festival.",
        "Manila is a culturally diverse city, with a mix of indigenous Philippine, Spanish, and American influences. This diversity is reflected in the city's architecture, art, and culture, and has helped to shape the city's unique character and identity. Spanish influences stem from the 16th century when the Spanish coloni8zed the Philippines and established Manila as a capital city. The Spanish then ruled the Philippines for over 300 years. On the other hand, in the late 19th century the Philippines became a terriroty of the United STates. Although the Philippines gained independence from the US in 1946, the country's close relationship has led to Manila adopting American influences."),

    "Seoul" : ("Soju is the most popular alcoholic beverage in Seoul and is often associated with Korean culture. It is a clear, vodka-like liquor that is made from rice, wheat, or barley, and is typically around 20% alcohol by volume, although some varieties can be as high as 45%. The flavor of soju can vary depending on the type of grain used to make it and the specific production process. It is often consumed neat, but it can also be mixed with other drinks or used as a base for cocktails.",
             "Seoul is home to the 'Namsan Love Lock Wall'. It is a wall covered with hundreds of locks, each one with the names of a couple inscribed on it. The tradition of leaving a lock at Namsan Tower as a symbol of love and commitment dates back to the 2000s and has become a popular activity for couples visiting the city. To participate in the tradition, couples write their names on a lock, attach it to the wall, and throw away the key as a symbol of their eternal love. The wall has become a popular spot for proposals and wedding photoshoots. Many people believe that leaving a lock at Namsan Tower will bring them good luck and a long-lasting relationship.",
             "Seoul hosts the Lotte World Mall, a large large shopping and entertainment complex in the middle of the city. It is considered one of the largest department stores in the world and covers over 500 000 square metres. The mall is home to over 500 stores, including international brands and local boutiques, as well as a wide range of restaurants and cafes. In addition to shopping and dining, the mall also features a number of attractions, such as an ice rink, a movie theater, and a water park."),

    "Kyoto" : ("Kyoto was the capital of Japan for more than 1,000 years, from 794 to 1868. In 1868 the government moved the capital of Japan to Tokyo. Reasons for this move included location, as Tokyo was easier to defend against any foreign threats. Anothe reason was the city's access to transportation and communication networks, which made it easier to govern the country. In addition, the government saw Tokyo as a more modern and forward-thinking city that was better suited to serve as the center of the government.",
             "Kyoto is home to more than 2,000 temples and shrines, many of which are associated with Buddhism and Shintoism.Some of the most famous temples and shrines in Kyoto include the Kinkaku-ji Temple, also known as the 'Golden Pavilion', and the Ginkaku-ji Temple, also known as the 'Silver Pavilion'.",
             "Kyoto hosts several alcohol related festivals sucha s the Kyoto Craft Beer and Sake Festival showcasing various local and international craft beers and sake, the Kyoto Cocktail Festival, the Kyoto Sake and Shochu Festival, and the Kyoto Wine Festival."),

    "Brisbane" : ("Brisbane is home to a number of sporting teams, including the Brisbane Broncos, a professional rugby league team and the professional soccer team, three time A-League Champions the Brisbanme Roar",
                "Brisbane is known for its subtropical climate and is home to a number of parks and gardens, including the Brisbane Botanic Gardens and the Roma Street Parkland. These and other green spaces offer a chance to enjoy the outdoors and experience the city's subtropical environment.",
                "Brisbane is located in close proximity to a number of other popular destinations in Queensland, such as the Gold Coast and the Sunshine Coast, which are both within a short drive of Brisbane."),

    "Townsville" : ("Townsville is the largest city in the region of North Queensland, with a population of approximately 180 000 people. The city is located in tropical north Queensland and is known for its warm climate and beautiful beaches. Access to the Great Barrier Reef is also made possible via a number of tour operators and boat charters based in Townsville that offer transportation between locations.",
                  "Townsville is home to a number of events and festivals throughout the year, which offer a chance to experience the city's diverse culture and vibrant community. Examples include the Australian Festival of Chamber Music, the Townsville Cultural Festival, the Townsville Food and Wine Festival and the Townsville Show, which features agricultural and livestock displays.",
                  "Townsville is located in the tropical north of Queensland, Australia and is in close proximity to a number of important strategic locations, including the South Pacific and Southeast Asia. This makes it an important location for the military to base its operations. The city hosts a strong Australian military presence, with several facilities located in the region. Notable examples include the Roytal Australian Air Force Base in Townsville and the HMAS Cairns."),

    "Sydney" : ("Sydney is home to a number of iconic landmarks including the Sydney Opera HOuse, a UNESCO World Heritage Site known for its distinctive sail-like roofs, and the Sydney Harbour Bridge, an important transportation link carrying road, rail and pedestrian traffic across the Sydney Harbour.",
              "Sydney is home to a number of festivals including the Sydney Festival, the Sydney Mardi Gras - a celebration fo LGBTQ+ culture and diversity, the Sydney Film Festival, the Sydney Writers' Ferstival and trhe Sydney Biennale."),

    "Yuzhno_Sakhalinsk" : ("Yuzhno-Sakhalinsk is a Russian city, and the largest city in the region of Sakhalin Oblast. Founded in 1882, it is now a modern city with a population of around 180 000 people. Due to it's location off the coast of Russia, a fascinating trivia is that it is possible to travel from the most Northern point of Japan to Yuzhno-Sakhalinsk within 7 hours by a combination of boat and bus, meaning on a technicality it is possible to go from Japan to Russia in 7 hours!",
                           "Yuzhno-Sakhalinsk is a Russian city, and the largest city in the region of Sakhalin Oblast. Founded in 1882, it is now a modern city with a population of around 180 000 people. Due to it's location off the coast of Russia, a fascinating trivia is that it is possible to travel from the most Northern point of Japan to Yuzhno-Sakhalinsk within 7 hours by a combination of boat and bus, meaning on a technicality it is possible to go from Japan to Russia in 7 hours!"),

    "Levuka" : ("Levuka is a town located on the island of Ovalau in the Lomaiviti Province of Fiji. It was the former capital of Fiji and the country's first official capital when it was declared a British colony in 1874.",
              "Levuka is home to a number of incredible festivals such as the Levuka Day Celebrations, the Levuka Carnival, the Levuka Food and Cultural Festival and the Levuka Town CUltural Tour, which offers tourists a chance to experience traditional Fijian life, including traditional dancing, singing and storytelling!"),

    "Auckland" : ("Auckland is known for its natural beauty and is home to a number of parks and reserves that offer a range of outdoor recreational activities. Some notable spots include the Waitakere Ranges, a group of rugged hills that can be hiked that offer incredible views of the surrounding area, the Auckland Domain, the city's oldest park, the Auckland Botanic Gardens and the Cornwall Park.",
                "Auckland is the largest city in New Zealand and is home to a population of around 1.7 million people. The city is located on the North Island of New Zealand and is the largest urban area in the country. The city additionally has a long history of immigration from Asian countries, which have led to a notable Asian community being established in the city."),

    "Kiritimati" : ("Kiritimati (also known as Christmas Island) is an atoll located in the Pacific Ocean, about halfway between Hawaii and Australia. It is the largest coral atoll in the world and is a part of the Republic of Kiribati. Kiritimati is known for its beautiful beaches and crystal clear waters, which make it a popular destination for scuba diving and other water sports. The atoll is also home to a number of species of birds and other wildlife, including the coconut crab, which is the largest land-living arthropod in the world.",
                  "Kiritimati, despite being known as Christmas Island, is a different location to the Australian external territory called the Territory of Christmas Island. This entire island is considered a Wildlife Sanctuary, and access to certain areas of the Island is restricted. There is however a small amount of tourism, that allows for tourists to enjoy a relatively quiet getaway."),

    "Starbuck_Island" : ("Starbuck Island is a small coral atoll located in the Pacific Ocean, about 2,500 kilometers southeast of Fiji. The atoll is a part of Kiribati and is one of the smallest and most remote inhabited islands in the world, hosting a population of around 50 people. The main economic activity on the island is fishing, and the island is also known for its beautiful beaches and crystal clear waters, which make it a popular destination for scuba diving and other water sports.",
                       "Starbuck Island has several stories on the origin of its name, none of which include the popular brand 'Starbucks'. Theories on the origins of the name 'Starbuck' include the idea is  was named after a character in the novel 'Moby-Dick,' which was written by Herman Melville and was popular among American whalers in the 19th century. Another theory is that the atoll was named after a real person, possibly a whaling captain or other sailor who visited the island."),

}


IM_THE_MAP_IM_THE_MAP_IM_THE_MAP_IM_THE_MAP_IM_THE_MAP_IM_THE_MAP_IM_THE_MAP_IM_THE_MAP_IM_THE_MAP = {
    "Baker_Island" : "Baker_Island_Trans.png",
    "Howland_Island" : "Howland_Island_Trans.png",
    "Pago_Pago" : "Pago_Pago_Trans.png",
    "Alofi" : "Alofi_Trans.png",
    "Swains_Island" : "Swains_Island_Trans.png",
    "Honolulu" : "Honolulu_Trans.png",
    "Waipahu" : "Waipahu_Trans.png",
    "Avarua" : "Avarua_Trans.png",
    "Juneau" : "Juneau_Trans.png",
    "Sitka" : "Sitka_Trans.png",
    "Nome" : "Nome_Trans.png",
    "Tijuana" : "Tijuana_Trans.png",
    "Seattle" : "Seattle_Trans.png",
    "Vancouver" : "Vancouver_Trans.png",
    "Denver" : "Denver_Trans.png",
    "San_Luis_Rio_Colorado" : "San_Luis_Rio_Colorado_Trans.png",
    "Sierra_Vista" : "Sierra_Vista__Trans.png",
    "Chicago" : "Chicago__Trans.png",
    "Quetzaltenango" : "Quetzaltenango_Trans.png",
    "Austin" : "Austin_Trans.png",
    "Philadelphia" : "Philadelphia_Trans.png",
    "Detroit" : "Detroit_Trans.png",
    "Lexington" : "Lexington_Trans.png",
    "Caracas" : "Caracas_Trans.png",
    "Mayaguez" : "Mayaguez_Trans.png",
    "Riberalta" : "Riberalta_Trans.png",
    "Buenos_Aires" : "Buenos_Aires_Trans.png",
    "Rio_de_Janeiro" : "Rio_de_Janeiro_Trans.png",
    "Vitoria_da_Conquista" : "Vitoria_da_Conquista_Trans.png",
    "Fernando" : "Fernando_Trans.png",
    "Praia" : "Praia_Trans.png",
    "Flores_Island" : "Flores__Trans.png",
    "London" : "London_Trans.png",
    "Dublin" : "Dublin_Trans.png",
    "Grenoble" : "Grenoble_Trans.png",
    "Vienna" : "Vienna_Trans.png",
    "Athens" : "Athens_Trans.png",
    "Kiev" : "Kiev_Trans.png",
    "Suez" : "Suez_Trans.png",
    "Istanbul" : "Istanbul_Trans.png",
    "Ryazan" : "Ryazan_Trans.png",
    "Dubai" : "Dubai_Trans.png",
    "Qazax" : "Qazax_Trans.png",
    "Oral" : "Oral_Trans.png",
    "Karachi" : "Karachi_Trans.png",
    "Dhaka" : "Dhaka_Trans.png",
    "Mirny" : "Mirny_Trans.png",
    "Jakarta" : "Jakarta_Trans.png",
    "Bangkok" : "Bangkok_Trans.png",
    "Shanghai" : "Shanghai_Trans.png",
    "Manila" : "Manila_Trans.png",
    "Seoul" : "Seoul_Trans.png",
    "Kyoto" : "Kyoto_Trans.png",
    "Brisbane" : "Brisbane_Trans.png",
    "Townsville" : "Townsville_Trans.png",
    "Sydney" : "Sydney_Trans.png",
    "Yuzhno_Sakhalinsk" : "Yuzhno_Trans.png",
    "Levuka" : "Levuka_Trans.png",
    "Auckland" : "Auckland_Trans.png",
    "Kiritimati" : "Kiritimati_Trans.png",
    "Starbuck_Island" : "Starbuck_Trans.png"
}

GMT_p_12_city = ['Baker_Island', 'Howland_Island']
GMT_p_11_city = ['Pago_Pago', 'Alofi', 'Swains_Island']
GMT_p_10_city = ['Honolulu', 'Waipahu', 'Avarua']
GMT_p_9_city = ['Juneau', 'Sitka', 'Nome']
GMT_p_8_city = ['Tijuana', 'Seattle', 'Vancouver']
GMT_p_7_city = ['Denver', 'San_Luis_Rio_Colorado', 'Sierra_Vista']
GMT_p_6_city = ['Chicago', 'Quetzaltenango', 'Austin']
GMT_p_5_city = ['Philadelphia', 'Detroit', 'Lexington']
GMT_p_4_city = ['Caracas', 'Mayaguez', 'Riberalta']
GMT_p_3_city = ['Buenos_Aires', 'Rio_de_Janeiro', 'Vitoria_da_Conquista']
GMT_p_2_city = ['Fernando']
GMT_p_1_city = ['Praia', 'Flores_Island']
GMT0_city = ['London', 'Dublin']
GMT_m_1_city = ['Grenoble', 'Vienna']
GMT_m_2_city = ['Athens', 'Kiev', 'Suez']
GMT_m_3_city = ['Istanbul', 'Ryazan']
GMT_m_4_city = ['Dubai', 'Qazax']
GMT_m_5_city = ['Karachi', 'Oral']
GMT_m_6_city = ['Dhaka', 'Mirny']
GMT_m_7_city = ['Jakarta', 'Bangkok']
GMT_m_8_city = ['Shanghai', 'Manila']
GMT_m_9_city = ['Seoul', 'Kyoto']
GMT_m_10_city = ['Brisbane', 'Townsville']
GMT_m_11_city = ['Sydney', 'Yuzhno_Sakhalinsk']
GMT_m_12_city = ['Levuka']
GMT_m_13_city = ['Auckland']
GMT_m_14_city = ['Kiritimati', 'Starbuck Island']

GMT_p_12 = datetime.now(pytz.timezone('Etc/GMT+12'))
GMT_p_11 = datetime.now(pytz.timezone('Etc/GMT+11'))
GMT_p_10 = datetime.now(pytz.timezone('Etc/GMT+10'))
GMT_p_9 = datetime.now(pytz.timezone('Etc/GMT+9'))
GMT_p_8 = datetime.now(pytz.timezone('Etc/GMT+8'))
GMT_p_7 = datetime.now(pytz.timezone('Etc/GMT+7'))
GMT_p_6 = datetime.now(pytz.timezone('Etc/GMT+6'))
GMT_p_5 = datetime.now(pytz.timezone('Etc/GMT+5'))
GMT_p_4 = datetime.now(pytz.timezone('Etc/GMT+4'))
GMT_p_3 = datetime.now(pytz.timezone('Etc/GMT+3'))
GMT_p_2 = datetime.now(pytz.timezone('Etc/GMT+2'))
GMT_p_1 = datetime.now(pytz.timezone('Etc/GMT+1'))
GMT0 = datetime.now(pytz.timezone('Etc/GMT'))
GMT_m_1 = datetime.now(pytz.timezone('Etc/GMT-1'))
GMT_m_2 = datetime.now(pytz.timezone('Etc/GMT-2'))
GMT_m_3 = datetime.now(pytz.timezone('Etc/GMT-3'))
GMT_m_4 = datetime.now(pytz.timezone('Etc/GMT-4'))
GMT_m_5 = datetime.now(pytz.timezone('Etc/GMT-5'))
GMT_m_6 = datetime.now(pytz.timezone('Etc/GMT-6'))
GMT_m_7 = datetime.now(pytz.timezone('Etc/GMT-7'))
GMT_m_8 = datetime.now(pytz.timezone('Etc/GMT-8'))
GMT_m_9 = datetime.now(pytz.timezone('Etc/GMT-9'))
GMT_m_10 = datetime.now(pytz.timezone('Etc/GMT-10'))
GMT_m_11 = datetime.now(pytz.timezone('Etc/GMT-11'))
GMT_m_12 = datetime.now(pytz.timezone('Etc/GMT-12'))
GMT_m_13 = datetime.now(pytz.timezone('Etc/GMT-13'))
GMT_m_14 = datetime.now(pytz.timezone('Etc/GMT-14'))

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()


    def button_clicked(self):
        Time_warp_list = [GMT_p_12, GMT_p_11, GMT_p_10, GMT_p_9,
                          GMT_p_8, GMT_p_7, GMT_p_6, GMT_p_5,
                          GMT_p_4, GMT_p_3, GMT_p_2, GMT_p_1,
                          GMT0, GMT_m_1, GMT_m_2, GMT_m_3,
                          GMT_m_4, GMT_m_5, GMT_m_6, GMT_m_7,
                          GMT_m_8, GMT_m_9, GMT_m_10, GMT_m_11,
                          GMT_m_12, GMT_m_13, GMT_m_14]

        The_chosen_one = []
        Cities = []

        for One_timezone in Time_warp_list:
            if One_timezone.hour == 17:
                The_chosen_one.append(datetime.tzname(One_timezone))
            else:
                pass

        if len(The_chosen_one) >= 2:
            The_chosen_one.pop(random.randrange(len(The_chosen_one)))
        else:
            pass

        # If the timezone is at 17 hours, add it to a list.
        for This_timezone_is_5pm in The_chosen_one:
            if This_timezone_is_5pm == "-12":
                Cities.append(random.choice(GMT_p_12_city))
            elif This_timezone_is_5pm == "-11":
                Cities.append(random.choice(GMT_p_11_city))
            elif This_timezone_is_5pm == "-10":
                Cities.append(random.choice(GMT_p_10_city))
            elif This_timezone_is_5pm == "-09":
                Cities.append(random.choice(GMT_p_9_city))
            elif This_timezone_is_5pm == "-08":
                Cities.append(random.choice(GMT_p_8_city))
            elif This_timezone_is_5pm == "-07":
                Cities.append(random.choice(GMT_p_7_city))
            elif This_timezone_is_5pm == "-06":
                Cities.append(random.choice(GMT_p_6_city))
            elif This_timezone_is_5pm == "-05":
                Cities.append(random.choice(GMT_p_5_city))
            elif This_timezone_is_5pm == "-04":
                Cities.append(random.choice(GMT_p_4_city))
            elif This_timezone_is_5pm == "-03":
                Cities.append(random.choice(GMT_p_3_city))
            elif This_timezone_is_5pm == "-02":
                Cities.append(random.choice(GMT_p_2_city))
            elif This_timezone_is_5pm == "-01":
                Cities.append(random.choice(GMT_p_1_city))
            elif This_timezone_is_5pm == "GMT":
                Cities.append(random.choice(GMT0_city))
            elif This_timezone_is_5pm == "+01":
                Cities.append(random.choice(GMT_m_1_city))
            elif This_timezone_is_5pm == "+02":
                Cities.append(random.choice(GMT_m_2_city))
            elif This_timezone_is_5pm == "+03":
                Cities.append(random.choice(GMT_m_3_city))
            elif This_timezone_is_5pm == "+04":
                Cities.append(random.choice(GMT_m_4_city))
            elif This_timezone_is_5pm == "+05":
                Cities.append(random.choice(GMT_m_5_city))
            elif This_timezone_is_5pm == "+06":
                Cities.append(random.choice(GMT_m_6_city))
            elif This_timezone_is_5pm == "+07":
                Cities.append(random.choice(GMT_m_7_city))
            elif This_timezone_is_5pm == "+08":
                Cities.append(random.choice(GMT_m_8_city))
            elif This_timezone_is_5pm == "+09":
                Cities.append(random.choice(GMT_m_9_city))
            elif This_timezone_is_5pm == "+10":
                Cities.append(random.choice(GMT_m_10_city))
            elif This_timezone_is_5pm == "+11":
                Cities.append(random.choice(GMT_m_11_city))
            elif This_timezone_is_5pm == "+12":
                Cities.append(random.choice(GMT_m_12_city))
            elif This_timezone_is_5pm == "+13":
                Cities.append(random.choice(GMT_m_13_city))
            elif This_timezone_is_5pm == "+14":
                Cities.append(random.choice(GMT_m_14_city))
            else:
                Cities.append("Error: No Timezone identified.")

        if Cities[0] in City_List:
            self.City_name_label.setText("It's 5pm in " + Cities[0] + "!")
            self.City_name_label.move(400, 790)
            self.City_name_label.setFont(QFont("Times", 18))
            self.City_name_label.adjustSize()
            self.City_name_label.setWordWrap(False)


            self.Description_label.setText("\n\nSpeaking of " + Cities[0] +
                               " did you know: \n" + random.choice(City_List[Cities[0]]))
            self.Description_label.setWordWrap(True)
            self.Description_label.setFont(QFont("Times", 15))
            self.Description_label.move(150, 810)
            self.Description_label.setAlignment(Qt.AlignCenter)

            value = IM_THE_MAP_IM_THE_MAP_IM_THE_MAP_IM_THE_MAP_IM_THE_MAP_IM_THE_MAP_IM_THE_MAP_IM_THE_MAP_IM_THE_MAP[Cities[0]]
            self.world_pixmap = QPixmap(value)
            self.world_image.setPixmap(self.world_pixmap)
            self.world_image.move(100, -90)
            self.world_image.resize(self.world_pixmap.width(),
                                    self.world_pixmap.height())
        else:
            pass


    def update_minutes(self):
        minute_now = datetime.now().minute
        if minute_now < 10:
            result_minutes = '%02d' % minute_now
        else:
            result_minutes = str(minute_now)
        self.Time_label.setFont(QFont("Times", 50))
        self.Time_label.setText("17:" + str(result_minutes))
        self.Time_label.move(420, 650)
        self.Time_label.adjustSize()
        self.update()


    def initUI(self):
        #Set window size
        self.setGeometry(750, 100, 1000, 1200)
        self.setWindowTitle("Where is it 5pm in the world")
        self.setStyleSheet('background-color: #121212')

        # Set image label
        self.world_image = QLabel(self)
        self.world_image.setPixmap(QPixmap("Drinks_2.png"))
        self.world_image.move(365, 140)
        self.world_image.adjustSize()

        #Set initial message when window opens
        self.Description_label = QLabel(self)
        self.Description_label.setText("Find out where in the world it's 5pm!")
        self.Description_label.setFont(QFont("Times", 50))
        self.Description_label.setStyleSheet("color: #9dc7c9")
        self.Description_label.setWordWrap(True)
        self.Description_label.adjustSize()
        self.Description_label.move(255,450)

        #Place holder for message that appears when button is pressed
        self.City_name_label = QLabel(self)
        self.City_name_label.setText("")
        self.City_name_label.setStyleSheet("color: #9dc7c9")
        self.City_name_label.setWordWrap(True)
        self.City_name_label.move(420, 690)

        #Clock showing the time in 17:00
        self.Time_label = QLabel(self)
        minute_now = datetime.now().minute
        self.Time_label.setFont(QFont("Times", 50))
        if minute_now < 10:
            result_minutes = '%02d' % minute_now
        else:
            result_minutes = str(minute_now)
        self.Time_label.setText("17:" + str(result_minutes))
        self.Time_label.setStyleSheet("color: #9dc7c9")
        self.Time_label.adjustSize()
        self.Time_label.move(420, 650)

        #Button that activates the function to sort through list of cities
        self.button = QtWidgets.QPushButton(self)
        self.button.setStyleSheet('background-color: #cfa86b')
        self.button.setText("Press me!")
        self.button.setFont(QFont("Times", 15))
        self.button.setGeometry(420, 730, 170, 50)
        self.button.clicked.connect(self.button_clicked)
        self.button.clicked.connect(self.update_minutes)


    def update(self):
        self.Description_label.adjustSize()
        self.City_name_label.adjustSize()

def window():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setWindowIcon(QIcon('Drinks_favicon.ico'))
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()