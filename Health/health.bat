cd Data
cd covid-19-Data
git fetch
git pull

cd..
cd..

py Scripts/covid_cases.py
py Scripts/covid_deaths.py
py Scripts/publish_health_data.py

cd Updates

git add *
git commit -a -m "COVID Update %date%-%time%"
git status

git push

cd..
