def top_countries(n=20):
    import pandas as pd
    data=pd.read_csv("dataset_countrywise.csv")
    country_wise=data.groupby("Country_Region").sum()
    df=country_wise.nlargest(n, 'Confirmed')
    return df

df=top_countries()
pairs=[(country,confirmed) for country,confirmed in zip(df.index,df['Confirmed'])]
    


import folium
import pandas as pd
data= pd.read_csv("dataset_countrywise.csv")
country_wise=data[['Lat','Long_','Confirmed']]
country_wise=country_wise.dropna()



m=folium.Map(location=[28.644800, 77.216721],zoom_start=3)


def circle_maker(x):
    folium.Circle(location=[x[0],x[1]],radius=float(x[2]),color="red",popup='confirmed cases:{}'.format(x[2])).add_to(m)
    
    
    
country_wise.apply(lambda x:circle_maker(x),axis=1)


html_map=m._repr_html_()


from flask import Flask,render_template

app=Flask(__name__)


@app.route('/')


def home():
    return render_template("home.html",table=df, cmap=html_map,pairs=pairs)


if __name__=="__main__":
    app.run(debug=True)