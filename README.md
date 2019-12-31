# NEU 337 - Spring 2020 (53760)
# Programing and Data Analysis for Modern Neuroscience

**!!! PLEASE INSTALL Python and JupyterLab PRIOR TO THE FIRST CLASS** (see instructions below). If you run into any troubles, *DO NOT FRET*. First, post your questions on Canvas to get help. Second, talk to fellow students or come to office hours to get squared away. As long as you get everything installed by the end of the first week, you should be fine.

## Course Objective

*The ability to read and write are obvious fundamental skills critical to all academic and quantitative pursuits.* **Fast approaching this level of fundamental importance is the ability to write computer programs to analyze and manipulate data sets ever increasing in richness and size.** This skillset is necessary to work with a wide array of systems whose models and behavior are sufficienlty complex to make analysis by hand intractable.

**In this course you will translate problems into code applying modern approaches for data analysis, statistical inference and modeling to various levels of neural systems and their component behavior.** We will use Python as a coding environment, and you will be exposed to resources and options for scientific computing.
 
 *Although geared for neuroscience, the approaches covered in this course are highly salient for a wide array of applications.*

## Course Details

* Time and Location: TR
* Instructor: Marcel Goldschen-Ohm
    * Office: NHB 4.352
    * Office hours: - If no one is in my office, check the conference room NHB 4.402 right around the corner!
    * **Please DO NOT email me directly!** Either message me through the course Canvas site or visit during office hours.
* TA: Augustin Hennings
    * Office hours:

## I'm confused, but my schedule makes attending office hours difficult. What do I do?

**!!! POST YOUR QUESTIONS ON CANVAS** where either myself or your fellow students can help. I may not reply immediately as advice from fellow students can often be the most illuminating.

## Course Prerequisites

There are no absolute prerequisites for the course, but you are expected to be familiar with basic mathematical functions and concepts, and you will be asked to perform quantitative calcualtions. Prior experience with programming and familiarity with matrix multiplication will be helpful, but is not necessary as they will be introduced.

## Requirements

* You must bring a laptop to class for hands on participation. If you do not own a laptop, contact your department or the College of Natural Sciences to obtain a loaner for the duration of the course.
* Install Python on the laptop you will bring to class (see instructions below).
* Attend class both motivated and prepared to work hard!
* Conduct yourself in a respectful manner at all times.
* Have fun!

## Academic Integrity

It is perfectly fine to work with your fellow students or anyone else on the homework assignments. If you do so, please include a note on your assignment indicating with whom you collaborated. Any academic dishonesty such as copying a fellow students assignment without collaborating in its completion will be severly punished as outlined by the University. **Most importantly, the ability to solve problems such as those in the homeworks is exactly the skillset you are here to obtain.** By not practicing these skills, you are primarily hurting yourself.

## Policies

* Students with disabilities may request appropriate academic accommodations from the Division of Diversity and Community Engagement, [Services for Students with Disabilities](http://www.utexas.edu/diversity/ddce/ssd/) (471-6259).

## Grading

| Homework | Exams   |
| -------- | ------- |
| 300 pts  | 200 pts |

## Syllabus

:warning: Please note that the syllabus is subject to change. It is your responsibility to attend class in order to know what is going on.

:construction: This syllabus is still a work in progress. Definitely look here first as there will be significant improvements, but the syllabus from last years course ([Spring 2019](https://github.com/marcel-goldschen-ohm/CompNeuroSpring2019)) will also give an impression of the topics to be covered.

29 lectures, Midterm exam, Final exam

* Jan-21-T: **Introduction to programming and Python.**
    * :cyclone: *Objectives:*
        * You will appreciate the need for programming in modern neuroscience.
        * You will be introduced to some good rules of thumb for programming.
        * You will be able to run Python code in the Jupyter notebook environemnt.
        * You will be able to associate values with appropriate variable types.
        * You will be able to index and iterate over lists of values.classmates.
        * You will understand the difference between mutable and immutable objects.
    * :pencil2: *Homework:*
        * (10 pts) homework-Jan-21-basics.ipynb (:alarm_clock: due *before* midnight Jan-28-T)
* Jan-23-R: **Working with NumPy multi-dimensional arrays (ndarray) - otherwise Python is just too slow and cumbersome. Also basic plotting with matplotlib.**
    * :cyclone: *Objectives:*
        * You will be able to import and use modules.
        * You will be able to manipulate multi-dimensional data arrays using NumPy ndarrays.
        * You will be able to extract/manipulate specific sections of data from ndarrays.
        * You will be able to perform operations on ndarrays without explicilty coding the operation for each element in the array.
        * You will be able to time your code.
        * You will explore how NumPy can accelerate your code.
        * You will appreciate that without NumPy, Python would NOT be a very useful language for science or data analysis.
        * You will be introduced to Numba as another method to accelerate code.
        * You will discuss the pitfall of unecessary code optimization.
        * You will be able to visualize data with basic plots in 2 or 3 dimensions.
    * :pencil2: *Homework:*
        * (10 pts) homework-Jan-23-numpy.ipynb (:alarm_clock: due *before* midnight Jan-30-R)
    * *Data Sets:*
        * Any multi-dimensional data? Perhaps several examples?
* Jan-28-T: **Pseudocode and Random Walk Lab - simulating molecular diffusion as a consequence of randomness.**
    * :cyclone: *Objectives:*
        * You will practice translating algorithms/word problems --> pseudo code --> code.
        * You will explore the benefits of using comments and variable names to enhance code readability with your fellow students.
        * You will be able to generate random numbers.
        * You will apply everything you've learned up to this point to simulate random walks in various dimensions and visualize them.
        * You will appreciate the role of randomness in molecular diffusion.
    * :pencil2: *Homework:*
        * (20 pts) homework-Jan-28-randomwalk.ipynb (:alarm_clock: due *before* midnight Feb-04-T)
    * *Data Sets:*
        * Visualize actual diffusion data?
* Jan-30-R: **Functions, zipping/unpacking, list comprehensions and classes (Object-Oriented Programming, OOP)**
    * :cyclone: *Objectives:*
        * You will be able to create and use functions.
        * You will be able to zip and unpack arrays.
        * You will be able to use list comprehensions.
        * You will be able to create and use classes.
        * You will appreciate that most available Python code is constructed as classes, so it's imperative to understand how they work even if you don't absolutely have to use them.
    * :pencil2: *Homework:*
        * (10 pts) homework-Jan-30.ipynb (:alarm_clock: due *before* midnight Feb-06-R)
    * *Extra Credit:*
        * Generators. Why the bother?
* Feb-04-T: **Probability Density/Mass Functions (PDFs/PMFs)**
    * :cyclone: *Objectives:*
        * You will understand how randomness can give rise to normally or exponentially distributed observations.
        * You will be able to obtain a probability from a PDF.
        * You will understand the difference between a probability and a likelihood.
        * You will be able to obtain parameters for normal or exponential PDFs that maximize their likelihood of explaining some data.
        * You will be able to plot data distributions overlaid with best fit PDFs.
        * You will understand how randomness can give rise to binomially or poisson distributed observations.
        * You will understand the difference between a PDF and a PMF.
        * You will be able to plot data distributions overlaid with best fit PMFs.
    * :pencil2: *Homework:*
        * (10 pts) homework-Feb-04.ipynb (:alarm_clock: due *before* midnight Feb-11-T)
    * *Data Sets:*
        * Normally distributed data. Drug efficacy?
        * Exponentially distributed data. Time intervals between neural spikes?
* Feb-06-R: **Curve Fitting and Maximum Likelihood Optimization**
    * *Objectives:*
        * You will be able to apply minimization algorithms to optimize the fit between a function and some data.
        * You will be able to enforce constraints such as parameter bounds and relations during optimization.
        * You will understand the benefit of working with loglikelihoods instead of likelihoods.
        * You will apply these concepts to obtain parameters for binomial or poisson PMFs that maximize their likelihood of explaining some data.
    * :pencil2: *Homework:*
        * (10 pts) homework-Feb-06.ipynb (:alarm_clock: due *before* midnight Feb-13-R)
    * *Data Sets:*
        * Poisson distributed data. Neural firing rates?
        * Binomially distributed data. Single-molecule bleach steps.
* Feb-11-T: **Hypothesis Testing and the Central Limit Theorem**
    * :cyclone: *Objectives:*
        * You will understand how to formulate a null and alternative hypothesis.
        * You will understand what a p-value is.
        * You will understand how to interpret a p-value and how they are often misinterpreted.
        * You will be able to apply a t-test.
        * You will understand what sort of data a t-test is relevant for.
        * You will understand why the Central Limit Theorem implies that t-tests are useful in many, although not all, cases.
        * You will be able to describe types of data where t-tests are not likely to be applicable.
    * :pencil2: *Homework:*
        * (10 pts) homework-Feb-11.ipynb (:alarm_clock: due *before* midnight Feb-18-T)
    * *Data Sets:*
        * Independent and related samples for t-test. Maybe drug effects in new or same population as placebo.
    * *Extra Credit:*
        * Write code illustrating the Central Limit Theorem.
* Feb-13-R: **Bootstrap and Permutation tests**
    * :cyclone: *Objectives:*
        * You will be able to bootstrap a data set.
        * You will understand why bootstrapping is useful and under what circumstances it will not help you.
        * You will be able to apply a permutation test to a data set.
        * You will understand for what specific question a permutaion test is relevant.
        * You will understand the difference between parametric and nonparametric tests.
        * You will be able to list one benefit and one downside to nonparametric tests like bootstrap and permutation tests as compared to parameteric tests.
    * :pencil2: *Homework:*
        * (10 pts) homework-Feb-13.ipynb (:alarm_clock: due *before* midnight Feb-20-R)
    * *Data Sets:*
        * Time intervals between neural spikes before and after drug?
* Feb-18-T: **Timeseries**
    * :cyclone: *Objectives:*
        * You will be able to explain the concepts of sampling, Nyquist frequency, subsampling and aliasing.
        * You will be able to quantify the autocorrelation of a timeseries, and explain what it means.
        * You will be able to apply Fourier analysis to a time series and explain what the frequency domain features represent.
        * You will be able to predict how changes in frequency domain components will affect the time domain signal.
        * You will be able to plot a power spectrum for a timeseries and interpret it.
        * You will be able to plot a spectrogram for a timeseries and interpret it.
    * :pencil2: *Homework:*
        * (10 pts) homework-Feb-18.ipynb (:alarm_clock: due *before* midnight Feb-25-T)
    * *Data Sets:*
        * Brain EEG, cardiac EEG.
        * single cell membrane voltage in current-clamp.
        * Single channel recording.
* Feb-20-R: **Filtering**
    * :cyclone: *Objectives:*
        * You will be able to filter a timeseries by manipulating its Fourier frequency domain.
        * You will be able to filter a timeseries by convolving it with another timeseries.
        * You will be able to predict the result of filtering by convolution with simple functions. 
        * You will be able to subsample without aliasing.
        * You will be able to visualize 2D images.
        * You will be able to filter 2D image filters using convolution.
        * Motivate: Convolutional Neural Networks (CNNs) that are the basis for most image recognition.
    * :pencil2: *Homework:*
        * (10 pts) homework-Feb-20.ipynb (:alarm_clock: due *before* midnight Feb-27-R)
* Feb-25-T: **Feature detection**
    * :cyclone: *Objectives:*
        * Detecting image features using filters.
        * Detecting timeseries features.
    * :pencil2: *Homework:*
        * (10 pts) homework-Feb-25.ipynb (:alarm_clock: due *before* midnight Mar-03-T)
    * *Data Sets:*
        * EEG, Single cell or field potential membrane voltage.
* Feb-27-R: **Hidden Markov Models (HMMs)**
    * :cyclone: *Objectives:*
        * Memoryless
        * Rate constants
        * Eyring transition state theory
        * Exponential (geometric) dwell time distributions
        * Number of distinguishable states
        * Filtering single molecule timeseries
    * :pencil2: *Homework:*
        * (10 pts) homework-Feb-27.ipynb (:alarm_clock: due *before* midnight Mar-05-R)
    * *Data Sets:*
        * Single-channel recordings --> discrete states
* Mar-03-T: **Hidden Markov Models (HMMs)**
    * :cyclone: *Objectives:*
        * Non-observable states
        * Gaussian Mixture Models (GMMs) <-- covered in clustering section
        * Baum-Welch optimization
        * Which model is best?
        * Bayesian and Akaike Information Criteria
    * :pencil2: *Homework:*
        * (10 pts) homework-Mar-03.ipynb (:alarm_clock: due *before* midnight Mar-10-T)
    * *Data Sets:*
        * Single cell membrane voltage --> refractory, approach threshold, spike
        * Neural spiking --> low activity, high activity, bursting
* Mar-05-R: **Hidden Markov Models (HMMs)**
    * :cyclone: *Objectives:*
    * :pencil2: *Homework (10 pts):*
        * homework-Mar-05.ipynb (:alarm_clock: due *before* midnight Mar-12-R)
* Mar-10-T: **Review**
* Mar-12-R: **Midterm Exam**
* Mar-17-T: SPRING BREAK
* Mar-19-R: SPRING BREAK
* Mar-24-T:
    * :cyclone: *Objectives:*
* Mar-26-R:
    * :cyclone: *Objectives:*
* Mar-31-T:
    * :cyclone: *Objectives:*
* Apr-02-R:
    * :cyclone: *Objectives:*
* Apr-07-T:
    * :cyclone: *Objectives:*
* Apr-09-R:
    * :cyclone: *Objectives:*
* Apr-14-T:
    * :cyclone: *Objectives:*
* Apr-16-R:
    * :cyclone: *Objectives:*
* Apr-21-T:
    * :cyclone: *Objectives:*
* Apr-23-R:
    * :cyclone: *Objectives:*
* Apr-28-T:
    * :cyclone: *Objectives:*
* Apr-30-R:
    * :cyclone: *Objectives:*
* May-05-T:
    * :cyclone: *Objectives:*
* May-07-R: **Review**
* May-??(13-16,18-19): Final Exam (date will be that scheduled by the University)

## Install Python (required)
1. Get the Anaconda Python distribution (**latest version 3.x**) from https://www.anaconda.com/download and just follow the install steps. Anaconda comes with a bunch of useful scientific libraries such as Numpy and Scipy that you would otherwise have to install yourself.
2. Launch Anaconda Navigator. Install JupyterLab and Spyder via the widgets in the Home tab. JupyterLab is a web-based python notebook and Spyder is an environment for running Python that is similar to MATLAB.


## Install R (optional)
1. Get R from https://cran.revolutionanalytics.com/index.html and run the installer.
2. Get RStuio Desktop from https://www.rstudio.com/. This is an environment for running R that is similar to MATLAB.


## Install Julia (optional)
I recommend just following the instructions at https://docs.junolab.org/latest/man/installation/. Get the latest stable release. I also recommend installing the Atom editor and Juno IDE.


## Install MATLAB (optional)
UT students have free access to MATLAB.

1. Go to www.mathworks.com and create a user account. **Your username MUST be your UT email address!**
2. Go to [UT Service Now](https://ut.service-now.com/utss/catalogoverview.do?sysparam_citems_id=f9d65c7c4ff9d200f6897bcd0210c77d&sysparam_cat_id=e0d08b13c3330100c8b837659bba8fb4,Information%20Technology&sys_click_name=features&sys_features=1) and request MATLAB. **Click the Request button in the MATLAB for Students Only box near the bottom of the page.** Your request may take a day or two to process, so don't delay.
3. Sign in to your mathworks account and you should see a license from UT is available to you. Use that license to download MATLAB (latest version). Then run the installer. If you can afford the space (>20 GB) *get all the toolboxes that you can*. If not, *get at least those toolboxes listed at https://www.mathworks.com/products.html under the MATLAB product family sections 'Math, Statistics, and Optimization', 'Signal Processing', 'Image Processing' and 'Computational Biology'.*

Note, once you've registered you can also use MATLAB via an online interface that mimicks the application environment at https://matlab.mathworks.com.


## Install GitHub Desktop (optional)
1. Go to https://github.com and create an account if you don't already have one.
2. Go to https://desktop.github.com and download the GitHub Desktop app.
3. Open the app and select File->Clone Repository. Select URL and enter the URL of this repository (https://github.com/marcel-goldschen-ohm/NEU337-Spring2020), then click 'Clone'. This will download all of the files in this repository to a folder on your computer. To navigate to the folder from GitHub Desktop select Repository->Show in Finder (that's for MacOS, wording may differ on Windows machines).
4. Whenever you want to make sure that you have the latest version of all files in the repository, select Repository->Pull to download ONLY what has changed since the last time you downloaded the repository.
5. *To make sure you do not overwrite any homework assignment files, I recommend copying all of the homeworks into a separate folder on your computer rather than editing the files directly in the GitHub repository folder.*

## Resources
* [Python Challenges](http://www.pythonchallenge.com): Fun! Will test your Python skills.
* [Computational and Inferential Thinking](https://www.inferentialthinking.com): Quick course on statistics and Python with examples. **This is a good place to start.**
* [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook): Explanations and examples. **This is also a good first learning tool.**
* [Computational Statistics in Python](http://people.duke.edu/~ccc14/sta-663-2017): Great collection of references with examples. Highly recommend! **Mostly for reference and code examples, but they're very useful.**
* [Statistics Done Wrong](https://www.statisticsdonewrong.com): **MUST READ!!!**
* [An Introduction to Statistical Learning](https://www-bcf.usc.edu/~gareth/ISL/ISLR%20First%20Printing.pdf): Nice intro to fairly complex statistical methods with very little math. **Highly recommend!** Example code is in R, but explanations are helpful in general. Note that this is a bit longer and more indepth than the options above. **This is more about understanding statistical methods than coding.**
