# 2020 CNU DataTon - 팀 메리 솔로스마스


## What we've done
  음식 관련 태그 중, 약 7000만개의 게시물이 존재하는 "#먹스타그램"선정.  
  인스타그램에서 "#먹스타그램" 태그를 기준으로, 연관 태그와 사람들이 언제 먹스타그램을 올리는지 분석

## Authors

* **hygoni** - *Data Crawling* - [Github](https://github.com/hygoni)
* **isaac-lee** - *Data Visualization* - [Github](https://github.com/isaac-lee)

## Expectations & Result
  처음 예상할 때는 "어떤 음식을 먹는지"와 관련된 데이터가 나올거라고 생각했으나,  
  실제로는 "음식과 관련된 인스타그램 태그들"이 나오는 걸 확인할 수 있었다.  
 
## Data Crawling
  ![Crawling](https://github.com/hygoni/DataTon/blob/main/images/crawling.PNG?raw=true)   
  실제로 데이터를 수집하는 모습  
  
## Data Visualization
  ![Tag Chart](https://github.com/hygoni/DataTon/blob/main/images/piechart.PNG?raw=true)  
  "#먹스타그램" 관련 태그의 분포 (Pie Chart)  
  
  ![Time Graph](https://github.com/hygoni/DataTon/blob/main/images/time_graph.PNG?raw=true)  
  먹스타그램을 올리는 시간대는 시간대는 아침 10시, 저녁 8시-12시 사이에 많이 분포한다.  

## Behind Story
  원래 멀티스레딩으로 구현하려고 shared resource를 lock으로 관리하고 노력을 좀 했다.  
  그런데 너무 빠른 속도로 데이터를 수집하니까 instagram에서 밴을 때렸다.  
  결국 1 스레드로 데이터를 수집했다 T.T  
  ** 크리스마스에 약속 없는거 실화인가요? **

## Built With

* [Python](https://python.org)
* [Selenium](https://www.selenium.dev/)
* [Chromedriver](https://chromedriver.chromium.org/downloads)
