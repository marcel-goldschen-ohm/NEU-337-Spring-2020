# NEU 337 - Spring 2020 (53760)
# Programing and Data Analysis for Modern Neuroscience

**!!! PLEASE INSTALL Python and JupyterLab PRIOR TO THE FIRST CLASS** (see instructions below). If you run into any troubles, *DO NOT FRET*. First, post your questions on Canvas to get help. Second, talk to fellow students or come to office hours to get squared away. As long as you get everything installed by the end of the first week, you should be fine.

## Course Objective

*The ability to read and write are obvious fundamental skills critical to all academic and quantitative pursuits.* **Fast approaching this level of fundamental importance is the ability to write computer programs to analyze and manipulate data sets ever increasing in richness and size.** This skillset is necessary to work with a wide array of systems whose models and behavior are sufficiently complex to make analysis by hand intractable.

**In this course you will translate problems into code applying modern approaches for data analysis, statistical inference and modeling to various levels of neural systems and their component behavior.** We will use Python as a coding environment, and you will be exposed to resources and options for scientific computing.
 
 *Although geared for neuroscience, the approaches covered in this course are highly salient for a wide array of applications.*
 
 ## Breadth over Depth
 
We will cover a wide array of topics rather than explore any one topic in great detail. Topics will be introduced at a level where you should be able to understand each concept and put them to use. However, realize up front that we may have only scratched the surface.

*The goal of the course is to give you enough of a basic toolset that you will have the necessary foundation to develop programs for any concept that you understand.*

## Course Details

* Time and Location: TR 2:00-3:30 PM, JGB 2.202
* Instructor: Marcel Goldschen-Ohm
    * Office: NHB 4.352
    * Office hours: R 3:30-5:00 PM, NHB 4.352 (or conference room 4.402 right around the corner)
    * **Please DO NOT email me directly!** Either message me through the course Canvas site or visit during office hours.
* TA: Augustin Hennings
    * Office hours (SEA 2.218 - Lewis-Peacock Lab):
        * W 1:45-3:15 PM 
        * R 10:00 AM-12:00 PM
    + Email: achennings@utexas.edu (Response within 24hrs - Please include `NEU337` in the subject line)
 
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

| Homework     | Exams   |
| ------------ | ------- |
| 200-300 pts  | 200 pts |

## Homework

Most homework will be in the form of Jupyter notebooks. Homework assignments will be posted on Canvas where you will be required to upload the completed notebook file. Be sure to name the file `your_full_name.ipynb` OR `your_eid.ipynb`. Also note that uploading to Canvas can sometimes be less than instantaneous, so DON'T WAIT UNTIL ONE MINUTE BEFORE MIDNIGHT ON THE DEADLINE TO SUBMIT.

## Syllabus

:warning: Please note that the syllabus is subject to change. It is your responsibility to attend class in order to know what is going on.

> 29 lectures, Midterm exam, Final exam

* Jan-21-T: **Introduction to programming and Python.**
    * :cyclone: *Objectives:*
        * You will appreciate the need for programming in modern neuroscience.
        * You will be introduced to some good rules of thumb for programming.
        * You will be able to run Python code in the Jupyter notebook environemnt.
        * You will be able to associate values with appropriate variable types.
        * You will be able to query and respond to true/false statements.
        * You will be able to index and iterate over lists of values.
    * :pencil2: *Homework:*
        * (10 pts) homework-Jan-21-basics.ipynb (:alarm_clock: due *before* midnight Jan-28-T)
* Jan-23-R: **Working with NumPy multi-dimensional arrays (ndarray) - otherwise Python is just too slow and cumbersome.**
    * :cyclone: *Objectives:*
        * You will be able to import and use modules.
        * You will be able to manipulate multi-dimensional data arrays using NumPy ndarrays.
        * You will be able to extract/manipulate specific sections of data from ndarrays.
        * You will be able to perform operations on ndarrays without explicilty coding the operation for each element in the array.
        * You will understand the difference between mutable and immutable objects.
    * :pencil2: *Homework:*
        * (10 pts) homework-Jan-23-numpy.ipynb (:alarm_clock: due *before* midnight Jan-30-R)
* Jan-28-T: **Timing your code and basic plotting with Matplotlib.**
    * :cyclone: *Objectives:*
        * You will be able to time your code.
        * You will explore how NumPy can accelerate your code.
        * You will appreciate that without NumPy, Python would NOT be a very useful language for science or data analysis.
        * You will be able to visualize data with basic plots using Matplotlib.
* Jan-30-R: **List comprehensions, Functions, Classes, Modules, and Numba**
    * :cyclone: *Objectives:*
        * You will be able to zip and unpack arrays.
        * You will be able to use list comprehensions.
        * You will be able to create and use functions.
        * You will be able to create and use classes.
        * You will be able to create and use modules.
        * You will appreciate that most available Python code is constructed as modules with classes, so it's imperative to understand how they work even if you don't absolutely have to use them.
        * You will be introduced to Numba as another method to accelerate code.
    * :pencil2: *Homework:*
        * (10 pts) homework-Jan-30-advanced.ipynb (:alarm_clock: due *before* midnight Feb-06-R)
    * *Extra Credit:*
        * (5 pts) extracredit-Jan-30-generators.ipynb (:alarm_clock: due *before* midnight Feb-06-R)
* Feb-04-T: **Pseudocode, Readability and Optimization** 
    * :cyclone: *Objectives:*
        * You will practice translating algorithms/word problems --> pseudo code --> code.
        * You will discuss the benefits of using comments and variable names to enhance code readability.
        * You will discuss the pitfall of unecessary code optimization.
    * :pencil2: *Homework:*
        * (8 pts) homework-Feb-04-pseudocode.ipynb (:alarm_clock: due *before* midnight Feb-11-T)
    * :pencil2: *Extra Credit:*
        * (4 pts) extracredit-Feb-04-quicksort.ipynb (:alarm_clock: due *before* midnight Feb-11-T)
* Feb-06-R: **Random Walk Lab - simulating molecular diffusion as a consequence of randomness.**
    * :cyclone: *Objectives:*
        * You will be able to generate random numbers.
        * You will apply everything you've learned up to this point to simulate random walks in various dimensions and visualize them.
        * You will appreciate the role of randomness in molecular diffusion.
    * :pencil2: *Homework:*
        * (20 pts) homework-Feb-06-randomwalk.ipynb (:alarm_clock: due *before* midnight Feb-18-T)
* Feb-11-T: **Probability Distributions of Random Variables**
    * :cyclone: *Objectives:*
        * You will understand the difference between discrete and continuous random variables.
        * You will understand the difference between probability mass functions (PMFs) and probability density functions (PDFs).
        * You will be able to obtain a probability from a PDF.
        * You will be able to obtain statistics such as mean and variance from a probability distribution.
        * You will be able to plot probability distributions.
        * You will understand that different processes give rise to different types of distributions of random variables.
        * You will be able to identify types of data described by binomial, poisson, exponential and normal distributions.
    * :pencil2: *Homework:*
        * (9 pts) homework-Feb-11-probdist.ipynb (:alarm_clock: due *before* midnight Feb-20-R)
* Feb-13-R: **Requested Review**
* Feb-18-T: **Canceled**
* Feb-20-R: **Curve Fitting, Optimization and Maximum Likelihood Estimation (MLE)**
    * *Objectives:*
        * You will be able to apply minimization algorithms to optimize the fit between a function and some data.
        * You will be able to enforce constraints such as parameter bounds and relations during optimization.
        * You will be able to fit model distributions to data to infer parameters of the distributions from which the random data samples were obtained.
        * You will understand the benefit of working with loglikelihoods instead of likelihoods.
        * You will apply these concepts to obtain maximum likelihood estimates for parameters of nontrivial probability distributions to samples of random variables.
    * :pencil2: *Homework:*
        * (10 pts) homework-Feb-20-mle.ipynb (:alarm_clock: due *before* midnight Feb-27-R)
* Feb-25-T: **Hypothesis Testing and the Central Limit Theorem**
    * :cyclone: *Objectives:*
        * You will understand how to formulate a null and alternative hypothesis.
        * You will understand what a p-value is.
        * You will understand how to interpret a p-value and how they are often misinterpreted.
        * You will be able to apply a t-test.
        * You will understand what sort of data a t-test is relevant for.
        * You will understand why the Central Limit Theorem implies that t-tests are useful in many, although not all, cases.
        * You will be able to describe types of data where t-tests are not likely to be applicable.
    * *Extra Credit:*
        * Write code illustrating the Central Limit Theorem.
* Feb-27-R: **Bootstrap and Permutation tests**
    * :cyclone: *Objectives:*
        * You will be able to bootstrap a data set.
        * You will understand why bootstrapping is useful and under what circumstances it will not help you.
        * You will be able to apply a permutation test to a data set.
        * You will understand for what specific question a permutaion test is relevant.
        * You will understand the difference between parametric and nonparametric tests.
        * You will be able to list one benefit and one downside to nonparametric tests like bootstrap and permutation tests as compared to parameteric tests.
* Mar-03-T: **Timeseries**
    * :cyclone: *Objectives:*
        * You will be able to explain the concepts of sampling, Nyquist frequency, subsampling and aliasing.
        * You will be able to quantify the autocorrelation of a timeseries, and explain what it means.
        * You will be able to apply Fourier analysis to a time series and explain what the frequency domain features represent.
        * You will be able to predict how changes in frequency domain components will affect the time domain signal.
        * You will be able to plot a power spectrum for a timeseries and interpret it.
        * You will be able to plot a spectrogram for a timeseries and interpret it.
    * :pencil2: *Homework:*
        * (10 pts) homework-Feb-18-timeseries.ipynb (:alarm_clock: due *before* midnight Feb-27-R)
* Mar-05-R: **Filtering**
    * :cyclone: *Objectives:*
        * You will be able to filter a timeseries by manipulating its Fourier frequency domain.
        * You will be able to filter a timeseries by convolving it with another timeseries.
        * You will be able to predict the result of filtering by convolution with simple functions. 
        * You will be able to subsample without aliasing.
        * You will be able to visualize 2D images.
        * You will be able to filter 2D image filters using convolution.
        * Motivate: Convolutional Neural Networks (CNNs) that are the basis for most image recognition.
* Mar-10-T: **TBA**
* Mar-12-R: **Midterm Exam**
* Mar-17-T: SPRING BREAK
* Mar-19-R: SPRING BREAK

* Mar-24-T: **Hidden Markov Models (HMMs)**
    * :cyclone: *Objectives:*
        * Memoryless
        * Rate constants
        * Eyring transition state theory
        * Exponential (geometric) dwell time distributions
        * Number of distinguishable states
        * Filtering single molecule timeseries
* Mar-26-R: **Hidden Markov Models (HMMs)**
    * :cyclone: *Objectives:*
        * Non-observable states
        * Gaussian Mixture Models (GMMs) <-- covered in clustering section
        * Baum-Welch optimization
        * Which model is best?
        * Bayesian and Akaike Information Criteria

Possible topics yet to be scheduled:

GitHub,
Debugging,
Linear Regression,
Multiple Linear Regression,
Ridge/Lasso Regression,
Cross Validation,
Nonlinear Regression,
Principal Comonent Analysis,
Classification,
Random Forest,
Neural Network,
Bayesian Probability,
GUIs

* Mar-24-T:
* Mar-26-R:
* Mar-31-T:
* Apr-02-R:
* Apr-07-T:
* Apr-09-R:
* Apr-14-T:
* Apr-16-R:
* Apr-21-T:
* Apr-23-R:
* Apr-28-T:
* Apr-30-R:
* May-05-T:
* May-07-R: **Review**
* May-??(13-16,18-19): Final Exam (date will be that scheduled by the University)

## Install Python (required)
1. Get the Anaconda Python distribution (**latest version 3.x**) from https://www.anaconda.com/download and just follow the install steps. Anaconda comes with a bunch of useful scientific libraries such as Numpy and Scipy that you would otherwise have to install yourself.
2. !!! MacOS Catalina ONLY !!! If you are running MacOS Catalina, you might run into this problem: Anaconda creates a `.bash_profile` file in your home directory that needs to be renamed to `.zprofile` in Catalina (does NOT apply to older versions of MacOS).
3. Launch Anaconda Navigator. Install JupyterLab and Spyder via the widgets in the Home tab. JupyterLab is a web-based python notebook and Spyder is an environment for running Python that is similar to MATLAB.


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
