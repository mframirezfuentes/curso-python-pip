import utils
import read_csv
import charts

def run():
  #obtención de información para bar chart

  data = read_csv.read_csv('data.csv')
  country = input("Ingrese un pais ==> ")

  result = utils.population_by_country(data, country)



  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'],labels,values)

  #obtención de información para pie chart
  data = read_csv.read_csv("data.csv")
  data = list(filter(lambda item: item['Continent']== 'South America', data))
  countries = list(map(lambda x: x['Country/Territory'],data))
  percentages = list(map(lambda x: x['World Population Percentage'],data))
  charts.generate_pie_chart(country['Country/Territory'],countries,percentages)
if __name__ == '__main__':
  run()
