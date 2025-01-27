# Analysing Engagement and Propagation of HPV Vaccine Disinformation on X
## Introduction
Human papillomavirus (HPV) is a common sexually transmitted infection connected to various cancers and genital warts. Some high-risk types can cause significant health problems, such as cancers of the cervix, vagina, penis, etc. HPV vaccine, namely Gardsail, can effectively prevent those infections, particularly types 16 and 18, which account for over 70% of cervical cancer instances. HPV vaccination is considered a highly cost-effective public health tool to eradicate cervical cancers globally, especially in less developed areas where the illness is most prevalent while screening and treatment are scarce (World Health Organization, 2024).​ 

Authentic health information has a positive impact on public education and healthcare. On the other hand, false information poses risks that can be exacerbated by social media. It will serve as an echo chamber, feeding people information that supports their worldview and escalating extremists. People may become victims due to a lack of health literacy and the inability to assess reliability. The quality of health news is also inconsistent, regardless of the sources used. This undermines public health and reduces vaccine uptake. To reduce the risks associated with misinformation, it is critical to identify it before it spreads (Swire-Thompson et al., 2020).

With the growing size and complexity of data, humanities studies have increasingly incorporated computational methods to enhance traditional workflows for tasks such as communication and text analysis. The collaborative approach helps better understand the impact of false information on vaccine hesitancy or resistance. This research aims to explore how stereotypes in disinformation regarding HPV vaccine on X shape public engagement by applying natural language processing (NLP) techniques. While many previous studies have focused on English social media posts, our work is a multilingual study using more recent data, which helps to compare the patterns of dissemination across cultures. 

## Literature Review
Health misinformation contradicts with the general agreement about a phenomenon among scientists. As new information becomes available with advancing technology and methods, the boundaries between what is true and what is not are continually shifting. Disinformation is a concerted or intentional attempt to spread false information for financial gain, influence, or fame. Because the purpose of a message is not always clear, it is challenging to distinguish between disinformation and misinformation (Swire-Thompson et al., 2020). 

The majority of literature states that their findings are consistent with one another. Tomaszewski et al. (2021)’s study showed that false HPV vaccine information and risk perceptions on Twitter (now X, corpus in English from December 2013 to December 2017) could be successfully detected by applying machine learning and NLP to create a number of classification models. In particular, the convolutional neural network model (CNN) performed the best. False information primarily consisted of loss-framed messages about the possible risks of vaccines which cover much more subjects than true information. 

By analysing English tweets from December 2019 to March 2020, Kornides et al. (2022) concluded that audience engagement (measured by the total number of likes, retweets, and replies) against vaccines is higher than that in favour of them. Additionally, tweets containing personal narratives tend to have higher engagement. The most common categories of disinformation or misinformation were negative health effects (59%), compulsory vaccination (19%), and vaccine ineffectiveness (14%). Death (23%) and unspecified harm or injury (51%) were the most common negative health effects tweets mentioned. These misinformation tweets also tend to be ambiguous and general.

Some common stereotypes regarding the HPV vaccine include but are not limited to: (1) The vaccine is exclusively for women. (2) The vaccine can cause death and paralysis (or some unknown side effects). (3) Vaccine ineffectiveness if there is already sexual experience. (4) Suspicion of the commercial intention by doctors and pharmaceutical companies. (5) Unawareness of the risk of cervical cancer and the necessity of vaccination for the non-vaccinated people with no gynaecological conditions in their family or social network (Siu et al., 2019).

## Dataset Description & Research Directions
The dataset was collected by web scraping X, presenting the information of the tweets, users and engagement of the tweets (likes, replies, mentions, reposts). In the raw dataset, over 20000 tweets were collected. After preprocessing and narrowing down the scope for research, our dataset includes 2108 tweets in three languages: English (1448), French (496) and Italian (162). The tweets we focus on include those discussing HPV vaccination, related conspiracy theories, opinions and disinformation. 
In investigating the dataset, we aim to understand the common disinformation and stereotypes regarding HPV vaccination, as well as the engagement of social media users with those disinformation and stereotypes across languages. Therefore, our research questions are:

#### RQ1: What are the primary topics of disinformation and stereotypes related to the HPV vaccine? How do these topics vary across different languages?  

#### RQ2:  How do social media users interact with disinformation and stereotypes about the HPV vaccine? In what ways does user engagement differ across languages?

In this project, several challenges may impact the completeness and accuracy of the results. First, as we analyze social media data, the prevalence of slang and regionally-specific language poses a significant obstacle (see Table 1). Computational tools such as Latent Dirichlet Allocation (LDA) and Natural Language Processing (NLP) are typically optimized for formal language, such as that found in newspapers, and may struggle to process informal or colloquial expressions effectively. This limitation could introduce variability into the results. Second, there is currently no reliable solution to address the presence of bot-generated content and interactions on the platform X. Consequently, we must operate under the assumption that all tweets and interactions are authored and produced by human users, which may not accurately reflect the true nature of the data.

## References:
Kornides, M. L., Badlis, S., Head, K. J., Putt, M., Cappella, J., & Gonzalez-Hernadez, G. (2022). Exploring content of misinformation about HPV vaccine on twitter. Journal of Behavioral Medicine, 46(1–2), 239–252. https://doi.org/10.1007/s10865-022-00342-1

Siu, J. Y., Fung, T. K. F., & Leung, L. H. (2019). Social and cultural construction processes involved in HPV vaccine hesitancy among Chinese women: a qualitative study. International Journal for Equity in Health, 18(1). https://doi.org/10.1186/s12939-019-1052-9

Tomaszewski, T., Morales, A., Lourentzou, I., Caskey, R., Liu, B., Schwartz, A., & Chin, J. (2021). Identifying false human papillomavirus (HPV) vaccine information and corresponding risk perceptions from Twitter: Advanced Predictive models. Journal of Medical Internet Research, 23(9), e30451. https://doi.org/10.2196/30451

UCLA. (n.d.). Negative Binomial Regression | R Data Analysis Examples. https://stats.oarc.ucla.edu/r/dae/negative-binomial-regression/
World Health Organization. (2024a, March 5). Human papillomavirus and cancer. https://www.who.int/news-room/fact-sheets/detail/human-papilloma-virus-and-cancer

World Health Organization. (2024b, March 5). Immunizing against HPV. https://www.who.int/activities/immunizing-against-hpv


