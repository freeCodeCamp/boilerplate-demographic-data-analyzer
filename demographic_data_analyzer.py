import pandas as pd

def calc_perc(a,b):
    # calcula el porcentaje y retorna ya con el redondeo
    val = (a*100)/b
    return round(val,1)

def calculate_demographic_data(print_data=True):
    # Read data from file
    bdda = None
    bdda = pd.read_csv('./adult.data.csv')
    bdda = bdda.rename(columns={
        "age":"age",
        "workclass":"workclass",
        "fnlwgt":"fnlwgt",
        "education":"education",
        "education-num":"educationnum",
        "marital-status":"maritalstatus",
        "occupation":"occupation",
        "relationship":"relationship",
        "race":"race",
        "sex":"sex",
        "capital-gain":"capitalgain",
        "capital-loss":"capitalloss",
        "hours-per-week":"hoursperweek",
        "native-country":"nativecountry",
        "salary":"salary"
    })

    # degrees higher
    hdg=['Bachelors', 'Masters', 'Doctorate']

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = bdda.value_counts(subset='race') # OK
    #race_count = cant_race.tolist()
    #print (race_count)

    # What is the average age of men?
    average_age_men = bdda.groupby(["sex"]).age.mean().round(1)[1] # OK

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = calc_perc(((bdda[bdda['education'] == 'Bachelors'].education).count()),(bdda.education.count())) # OK

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    gananM50=bdda.query('salary == ">50K"')
    ccea=gananM50.query("education==@hdg").education.count() # ganan >= 50K y tienen educacion avanzada
    cceb=gananM50.query("education!=@hdg").education.count() # ganan >= 50K y tienen educacion avanzada
    
    # print (ccea, hec)
    higher_education = bdda.query("education==@hdg").education.count() # OK
    lower_education = bdda.query("education!=@hdg").education.count() 

    # percentage with salary >50K
    higher_education_rich = calc_perc(ccea,higher_education)               # OK
    lower_education_rich =calc_perc(cceb,lower_education)   # no esta bien 

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = bdda.hoursperweek.min()
    # print('min_work_hours', min_work_hours)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = gananM50[gananM50.hoursperweek == min_work_hours].hoursperweek.count()
    # print('num_min_workers', num_min_workers)
    total_wk_min    = bdda[bdda.hoursperweek==min_work_hours].hoursperweek.count()
    # print('total_wk_min', total_wk_min)

    rich_percentage = calc_perc(num_min_workers,total_wk_min)

    # What country has the highest percentage of people that earn >50K?
    paises50k = [gananM50.groupby(["nativecountry"]).salary.count()][0]
    paisestot = [bdda.groupby(["nativecountry"]).salary.count()][0]
    paisesAnalisis=pd.DataFrame()
    paisesAnalisis["50kpaises"] = paises50k
    paisesAnalisis["todos"] = paisestot
    paisesAnalisis["porc50k"] = (paisesAnalisis["50kpaises"] * 100)/ paisesAnalisis["todos"]
    paisesAnalisis["indice"] = paisesAnalisis.index
    tt = paisesAnalisis.porc50k.max()
    tt1 = paisesAnalisis.indice[paisesAnalisis['porc50k'] == tt]
    highest_earning_country = tt1[0]
    highest_earning_country_percentage = round(paisesAnalisis.porc50k.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    india50occ = (bdda.query(('salary == ">50K"') and ('nativecountry == "India"')).occupation)
    occupindia = pd.DataFrame()
    occupindia["occuind"] = india50occ
    indiamp = pd.DataFrame()
    indiamp["cant"] = [occupindia.groupby(["occuind"]).occuind.count()][0]
    indiamp["indice"] = indiamp.index
    top_IN_occupation = indiamp[indiamp.cant == indiamp.cant.max()].indice[0]
    # print('top_IN_occupation', top_IN_occupation)
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
