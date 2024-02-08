from urllib.parse import urlparse

# List of URLs to test
urls = [
    # National
    "https://www.ndtv.com/india-news/pm-narendra-modi-mallikarjun-kharge-nirmala-sitharaman-white-paper-vs-black-paper-as-bjp-congress-spar-over-10-year-performance-5016399#pfrom=home-ndtv_topscroll",
    "https://www.indiatoday.in/business/story/india-100-billion-dollar-investment-deal-with-switzerland-norway-one-millon-jobs-2499103-2024-02-08",
    "https://www.thehindu.com/news/national/the-legal-dispute-over-varanasi-mathura-mosques-explained/article67808876.ece",
    "https://www.news18.com/viral/why-7-days-make-a-week-and-12-months-a-year-8770885.html",
    "https://www.deccanchronicle.com/dc-exclusive-vigilance-report-nails-kcr-govt-for-kaleshwaram-failures",
    "https://timesofindia.indiatimes.com/sports/cricket/news/ishan-kishan-training-in-baroda-amidst-speculation-over-absence-from-cricket/articleshow/107508908.cms",
    "https://www.hindustantimes.com/india-news/pm-modi-lauds-ex-pm-manmohan-singh-in-farewell-speech-the-way-he-has-guided-101707371745012.html",
    "https://www.livemint.com/market/stock-market-news/lic-share-price-hits-record-high-ahead-of-q3-results-today-buy-hold-or-book-profit-11707364442300.html",
    "https://www.deccanherald.com/india/rajasthan/youth-killed-after-cricket-match-in-rajasthans-jhalawar-2884534",
    "https://www.thenewsminute.com/andhra-pradesh/jagan-reddy-denies-making-andhra-pradesh-debt-ridden",

    #International
    "https://www.nytimes.com/2024/02/07/world/europe/ukraine-us-military-aid-russia.html",
    "https://edition.cnn.com/2024/02/08/europe/mariupol-hrw-report-putin-russia-ukraine-intl/index.html",
    "https://www.theguardian.com/world/2024/feb/07/netanyahu-rejects-gaza-ceasefire-deal-and-says-victory-is-within-reach-israel",
    "https://www.foxnews.com/us/preteen-boy-dies-1-day-after-enrolling-controversial-north-carolina-therapy-camp-suspicious-death",
    "https://www.bbc.com/news/uk-england-sussex-68226283",
    "https://www.dailymail.co.uk/wellness-us/nutrition/article-13057647/salmon-reduces-cholesterol-Mediterranean-diet.html",
    "https://www.washingtonpost.com/politics/2024/02/07/lawyers-supreme-court-trump-ballot-case/",
    "https://www.wsj.com/politics/national-security/u-s-strike-kills-iraq-militia-leader-behind-deadly-drone-attack-on-american-base-d6971744?mod=hp_lead_pos1",
    "https://www.usatoday.com/story/news/nation/2024/02/07/sat-exam-changes-2024/72323660007/",
    "https://www.huffpost.com/entry/heart-attack-nausea-symptom_l_65c10f9de4b0dbc806ad8a4b"

]

# Loop through each URL and extract domain names
for url in urls:
    parsed_url = urlparse(url)
    domain_name_parts = parsed_url.netloc.split('.')
    if len(domain_name_parts) > 1:
        domain_name = domain_name_parts[1]
    else:
        domain_name = domain_name_parts[0]

    print("Domain name:", domain_name)
    print()  # Add a newline for clarity

