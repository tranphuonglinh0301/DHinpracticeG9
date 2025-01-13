# Topic modeling
During this step of the project, we did the topic modelling separately for tweets by languages using LDA. In LDA, the text is considered a bag of word, and the topics are identified based on the frequency of words. This is also the most common topic modelling method. 

The content of the tweets are tokenized and then lemmatized. After that, the stopwords were removed to avoid confusion during topic division. Based on the available tokens, the tweets are classified into 10 different topics (each language). When working on the English dataset, we have done some trials to find out the optimal number of topic. 10 is chosen, due to the fact that it is not too many, and at the same time has a higher coherence score within each topics compared to 3 or 5 topics. 

The results of the topic modelling is represented as a set of words. Therefore, further analysis and research need to be done to come to a clear conclusion. 

## Results 
### English
* Topics:

(0, '0.049*"s" + 0.036*"new" + 0.021*"that" + 0.018*"order" + 0.015*"woman" + 0.014*"tweet" + 0.014*"bad" + 0.012*"join" + 0.012*"las" + 0.009*"entire"')

(1, '0.047*"video" + 0.027*"pipe" + 0.027*"take" + 0.025*"year" + 0.023*"watch" + 0.023*"see" + 0.017*"etc" + 0.015*"destroy" + 0.015*"never" + 0.015*"every"')

(2, '0.137*"wef" + 0.043*"world" + 0.026*"say" + 0.022*"one" + 0.019*"make" + 0.013*"start" + 0.011*"china" + 0.011*"russia" + 0.010*"another" + 0.009*"not"')

(3, '0.031*"full" + 0.023*"create" + 0.021*"support" + 0.015*"divide" + 0.012*"blackrock" + 0.012*"solution" + 0.011*"sugar" + 0.010*"comply" + 0.010*"vanguard" + 0.009*"yup"')

(4, '0.055*"nwo" + 0.032*"com" + 0.027*"want" + 0.021*"diedsuddenly" + 0.018*"minutecities" + 0.015*"vaccine" + 0.015*"push" + 0.015*"gardasil" + 0.014*"global" + 0.012*"nothing"')

(5, '0.026*"population" + 0.025*"let" + 0.018*"esg" + 0.018*"could" + 0.018*"australia" + 0.015*"puppet" + 0.011*"listen" + 0.011*"buy" + 0.010*"folk" + 0.010*"class"')

(6, '0.057*"plan" + 0.050*"covid" + 0.033*"part" + 0.025*"need" + 0.025*"well" + 0.019*"lie" + 0.018*"ukraine" + 0.018*"happen" + 0.016*"work" + 0.015*"back"')

(7, '0.023*"wake" + 0.019*"sdgs" + 0.016*"live" + 0.015*"news" + 0.015*"think" + 0.014*"king" + 0.012*"happy" + 0.012*"great" + 0.011*"town" + 0.011*"samaria"')

(8, '0.184*"agenda" + 0.024*"climatescam" + 0.016*"greatreset" + 0.014*"un" + 0.011*"people" + 0.011*"like" + 0.011*"control" + 0.011*"cbdc" + 0.010*"newworldorder" + 0.009*"we"')

(9, '0.060*"room" + 0.020*"poison" + 0.016*"vote" + 0.016*"tell" + 0.015*"come" + 0.015*"alle" + 0.015*"online" + 0.013*"accedi" + 0.013*"wka" + 0.013*"chatrooms"')
* Coherence score: 0.47080604581842794
### Italian
* Topics:

(0, '0.010*"lecciones" + 0.010*"ecologismo" + 0.010*"rituales" + 0.010*"farso" + 0.010*"figlio" + 0.010*"atrazina" + 0.010*"satanic" + 0.010*"industria" + 0.010*"namere" + 0.010*"banca"')

(1, '0.112*"agenda" + 0.032*"video" + 0.030*"piped" + 0.023*"il" + 0.016*"potere" + 0.016*"politico" + 0.016*"cos" + 0.015*"loro" + 0.012*"greatreset" + 0.012*"via"')

(2, '0.085*"il" + 0.058*"agenda" + 0.037*"uno" + 0.035*"di" + 0.030*"non" + 0.028*"a il" + 0.026*"di il" + 0.020*"che" + 0.018*"essere" + 0.017*"avere"')

(3, '0.043*"di" + 0.024*"stare" + 0.024*"Usa" + 0.022*"davos" + 0.014*"com" + 0.014*"vaccino" + 0.014*"tutto" + 0.014*"usare" + 0.014*"di il" + 0.010*"schwab"')

(4, '0.077*"si" + 0.036*"agenda" + 0.028*"leggere" + 0.028*"scrivere" + 0.019*"con" + 0.019*"soros" + 0.006*"accoglienza" + 0.006*"ghetto" + 0.006*"liberazione" + 0.006*"franceriots"')

(5, '0.060*"agenda" + 0.027*"il" + 0.024*"globalista" + 0.024*"com" + 0.024*"de" + 0.022*"france" + 0.017*"macrondemission" + 0.017*"macron" + 0.017*"mociondecensura" + 0.017*"manifestation"')

(6, '0.097*"gardasil" + 0.026*"di il" + 0.026*"vaccination" + 0.024*"il" + 0.023*"casa" + 0.022*"wef" + 0.020*"Poizon" + 0.020*"vaccin" + 0.019*"agenda" + 0.015*"energia"')

(7, '0.110*"gardasil" + 0.041*"da il" + 0.040*"son" + 0.033*"poi" + 0.026*"governo" + 0.022*"agendare" + 0.019*"agendo" + 0.011*"seguire" + 0.011*"Wef" + 0.011*"strategia"')

(8, '0.028*"il" + 0.022*"live" + 0.022*"novax" + 0.013*"agendere" + 0.013*"nwo" + 0.013*"tutto" + 0.012*"gardasil" + 0.011*"ora" + 0.009*"ficco" + 0.009*"culo"')

(9, '0.040*"agenda" + 0.027*"Russia" + 0.023*"rinnovabile" + 0.023*"sustainability" + 0.023*"energia" + 0.021*"energy" + 0.017*"pi" + 0.017*"europe" + 0.013*"di" + 0.013*"elettricit"')
* Coherence score: 0.45179699013097335
### French
* Topics:

(0, '0.030*"sant" + 0.021*"celui" + 0.017*"comment" + 0.017*"votre" + 0.014*"gardasil" + 0.012*"minute" + 0.012*"org" + 0.012*"ministre" + 0.011*"cancer" + 0.011*"mentir"')

(1, '0.071*"le" + 0.044*"de" + 0.031*"pas" + 0.026*"être" + 0.021*"il" + 0.020*"que" + 0.020*"avoir" + 0.019*"un" + 0.019*"ce" + 0.017*"gardasil"')

(2, '0.088*"le" + 0.034*"nouveau" + 0.031*"inefficace" + 0.025*"vaccin" + 0.024*"dangereux" + 0.023*"gardasil" + 0.022*"contre" + 0.021*"com" + 0.021*"ado" + 0.021*"danger"')

(3, '0.030*"odd" + 0.026*"le" + 0.022*"temps" + 0.020*"agender" + 0.015*"autre" + 0.012*"tre" + 0.011*"agenda" + 0.010*"raoult" + 0.009*"tr" + 0.009*"être"')

(4, '0.014*"sident" + 0.013*"promotion" + 0.013*"plainte" + 0.012*"pharmaceutique" + 0.011*"donn" + 0.008*"ind" + 0.008*"er" + 0.008*"merck" + 0.008*"lhumanit" + 0.008*"base"')

(5, '0.098*"de" + 0.097*"le" + 0.043*"gardasil" + 0.030*"un" + 0.026*"et" + 0.023*"pour" + 0.022*"être" + 0.020*"en" + 0.013*"vaccin" + 0.012*"il"')

(6, '0.026*"falloir" + 0.022*"agenda" + 0.015*"injecter" + 0.014*"jour" + 0.011*"travail" + 0.011*"passer" + 0.010*"sou" + 0.010*"sans" + 0.010*"population" + 0.009*"celer"')

(7, '0.033*"video" + 0.031*"piped" + 0.014*"odd" + 0.014*"moignage" + 0.012*"ici" + 0.011*"attali" + 0.010*"organisation" + 0.009*"changement" + 0.008*"agenda" + 0.007*"ong"')

(8, '0.056*"ni" + 0.030*"on" + 0.028*"gar" + 0.027*"fille" + 0.017*"vacciner" + 0.015*"tribu" + 0.015*"opinion" + 0.014*"dr" + 0.011*"cancer" + 0.008*"rard"')

(9, '0.066*"le" + 0.036*"de" + 0.032*"effet" + 0.029*"secondaire" + 0.028*"et" + 0.020*"pour" + 0.019*"gardasil" + 0.018*"grave" + 0.017*"vaccin" + 0.016*"par"')
* Coherence score: 0.4625807249433322
