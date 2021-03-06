# NETS213 Final Project
# Stress Relief: The Eternal Dilemma (STRED)

----

**STRED** is a project whose goal is to provide high quality tips, resources, and words of encouragement that will help reduce stress and anxiety caused by stressors individuals encounter every day. 

This project follows a multi-step process that consists of data aggregation, quality control, data analysis, and visual user-friendly display of results that will serve as a resource for people who are seeking advice on how to reduce the stress they experience. **STRED** is divided into following major components:

----

## Step 1: Survey Template
The first step of our project consists of aggregating data about the stressors. We decided to narrow down the group of people we will ask for their causes of stress to college students. In this step, we will create a survey template in which we will ask students about what stresses them the most. Later on, we will publish it on Piazza to get responses from our classmates. Depending on the response rate, we might also ask our fellow classmates from other classes or other Penn students by publishing the survey in various group chats and Penn Facebook groups in order to get the approximate number of responses that we will be satisfied with. The milestones for this step include:
- Generating the survey template to match the needs of our project.
- Aggregating a sufficient number of viable stressors from our peers via social media, Piazza, and various group chats.
With regard to difficulty, we believe this component is a **2 out of 4**.

## Step 2: Gathering feedback from students 
In this step, we will gather the responses we got from students in step 1 in order to use them later on for gathering useful advice from CrowdWorkers. At this step, we will also filter the results so that they can be used in next steps. To ensure that our project is using proper data, we propose the following steps:
- Collect the number of unique responses, and remove any irrelevant, overly-specific, or vague stressors that may cause issues during our HIT phase. 
- Filter the results so that we have the appropriate number of responses to create a valuable end-project. Our end goal is to aim for about twenty to forty unique responses so that we account for a variety of stressors and perform the proper quality control checks in Mechanical Turk. 
With regard to difficulty, we believe this component is a **3 out of 4**.

## Step 3: Creating a HIT with responses gathered from students
At this point, we will create a HIT and post it on Amazon Mechanical Turk. We will use data gathered from Penn students about the stressors, we will ask Turkers to provide words of encouragement, tips and resources that can be helpful in the situations that were given to them. Our milestones for this component are:
- Create the HIT with clear instructions and minimal room for error on the Turker side. 
- Submitting our HIT and making sure that we run the trial on stressors multiple times to ensure quality responses.
- Accruing the responses in CSV format.
With regard to difficulty, we believe this component is a **3 out of 4**. 

## Step 4: Quality Control
In step 4 of our project, we will create another HIT in which we will ask Turkers to validate the response provided from Workers in step 3 based on our guidelines. This is a step that serves as a quality control to our responses and will allow us to filter the responses provided so we can make sure we don???t give back answers that are not positive, helpful or encouraging. Of course, to perform the quality control tests, we plan to:
- Create the HIT, again with clear instructions on proper rating responses.
- Submitting the HIT and await Turker answers.
- Gathering the data in CSV format.
With regard to difficulty, we believe this component is a **2 out of 4**. 

## Step 5: Rating the responses
After we are done filtering the responses gathered, we would like to rate their utility. Here again we will create another HIT and we will ask Workers to rate the responses provided based on how helpful and relevant to the situation described they think they are. Similar to step 4, our milestones for this component are:
- Create the HIT, again with clear instructions on proper rating responses.
- Submitting the HIT and await Turker answers.
- Gathering the data in CSV format.
With regard to difficulty, we believe this component is a **2 out of 4**. 

## Step 6: Data analysis of the results and website creation 
At this step, we will analyze the data we got from all the steps of our project. We would want to see which responses Turkers ranked the highest, how many of the responses gathered were not helpful at all or irrelevant,  etc. After that, we want to create a website that could serve as a resource for people who submitted answers in step 1. They will be able to see the most helpful responses to the problems there, which will consist of words of encouragement, advice, or resources. This step has many moving pieces, and requires the coordination of the entire team to make sure that each component is completed and accurate. We propose the following:
- Analyze the data and provide valuable insights into the study.
- Find the proper libraries to analyze our data in an input / output manner.
- Create a visual representation of our work via a website.
- Deploy our website and open it up for public use. 
With regard to difficulty, we believe this component is a **4 out of 4**. 

----

## Raw Data
A survey was posted on the NETS213 Piazza to collect common university student stressors. The 10 most common responses were cleaned and formatted into the file `data/stressors.csv`. There are two columns: `stressor_1` and `stressor_2` which reflect the two problems displayed on one HIT (each task will require workers to provide advice for two different problems). 100 total responses (10 per stressor) were collected from workers and are in the file `data/stressor_responses_1.csv`.

----

## Quality Control
In order to check answers validated in Step 4, we will use an **EM algorithm** to label each stressor-response pair. Sample inputs to the EM algorithm can be found in `data/quality_control`. Our sample datasets are `qc_input1` and `qc_input2`. This is a cleaned-up version of the CSV's we expect to extract from the HITs. They have columns: `'WorkerId'`, `'Input.result[i]'`, `'Answer.results[i].Yes'`. The final labeled pairs we expect to output from the EM algorithm will have two columns: `'response'` and `'label'`. The labels gathered from workers will either by a `yes [1]` or `no [0]`. We have a total of ten different stressors. Each stressor will have it's own *independent input and output CSV* containing their respective responses and worker labels. In short, we will run the EM algorithm 10 times, one per stressor.

Our **EM Algorithm** reads a CSV of responses, and outputs another CSV of results. The columns of each I/O dataset is outlined above. To ensure convergence, our algorithm goes through one-thousand interations. For each iteration, we monitor `worker confusion matrices` and `weighted response labels` and update these two after each iteration of the algorithm. The first step of the algorithm is to take a weighted majority vote based on worker response and the confusion matrices. We then update the finalized labels for each response, and then adjust the confusion matrices based on the weighted majority. The algorithm goes through one-thousand loops of these iterations, and then finally returns the outputted CSV file.

----

## Data Aggregation Of Ratings of Responses
To choose the best responses that we filtered in the previous step, we asked multiple Turkers to rate them on the scale from 1 to 10. For each of the responses, we took the average of the Workers' responses.

----

## Guide On How To Complete The Validation HIT
We prepared a video that explains how to complete the validation HIT. You can find it [here](https://vimeo.com/541439387?fbclid=IwAR36QGOtnl9Tewa9etmJl1Zt2hh_3r2jbYO3U04osz76jM-tDewDk6ZvC1I). In this HIT, we ask you to answer if you would feel comfortable giving the advice provided to your family members or friends. If you think it is a good, thoughtful response that contains resources and words of encouragment you would answer Yes, otherwise you would answer No. You will be answering Yes or No to 14 advice responses that are responses to a single stressor college students experience. You can respond Yes or No to as many of them as you want. 

For example, if the stressor is: "I am worried about not finding a job or internship for next summer.".

One of the responses for thi stresssor could be "Finding a job or internship is very complex thing. It depends upon many external factors and mainly on the economic condition of the country. So, don't worry about the job, the important thing is to learn the skills required for getting a job. Just keep applying to the companies and take an effort on improving your skills. Definitely, you will get a nice job." if you think this is a good response you would answer yes. We think it is a good response because it consists of words of encouragment as well as advice on what the person should do. 

Another response could be "don't be in a hurry, all in your time, i will help you". In this case, we think the answer should be No. This response even though it consists some sort of words of encouragement, it is not specific enough, as well as it cannot be generalized to everyone who struggles with the problem presented.

----

## Directory
- `docs/flow_chart.png`: flow diagram of major system components
- `docs/mockups`: mockups of user-facing interfaces
- `data/stressors.csv`: student stressors collected from survey
- `data/stressor_responses1.csv`: responses to stressors collected through MTurk
- `data/quality_control`: sample quality control I/O datasets
- `data/aggregation`: sample aggregation module
  - `data/aggregation/Fake Data 2 - Sheet1.csv` : sample data for rating the responses
  - `data/aggregation/average_ratings.csv` : csv file we got after running averaging script
- `layouts`: HTML layouts for MTurk HIT's
- `src/quality_control`: EM algorithm script
- `src/average_ratings.py` : script for calculating average among the responses 
- `website/nets.css` : contains css of the website
- `website/nets.html`: contains HTML of the website

----

## Goal of Analysis

We plan to analyze the best stressor-response matches with crowdsourced responses for common stressors. The goal of this analysis is the identification of adequate and helpful ways to deal with stress and respond to stressors without requiring the assitance of mental healthcare professionals- a goal more important than before due to global issues such as the COVID-19 pandemic. We aggregate the responses to each stressor and then ask MTurk workers to first differentiate between appropriate and inappropriate matches, then ask another group of workers to rank each response for a stressor. Through this process and quality control, we find the best actions the crowd believes a person should take in the face of certain problems.

----
## Website

We created the website that would serve as a resource for people who submitted answers to our survey, as well as those who experience similar problems. We used HTML, CSS, and Bootstrap to create it. For each stressor, we chose the highest ranked response and published it on our website. Additionally website also contains redirection to Airtable to all responses gathered and their ratings for those who are interested to learn more! The website can be accessed [here](https://zuziamatysiak.github.io/STRED/).
