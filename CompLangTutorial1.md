
<img src=https://www.rstudio.com/wp-content/uploads/2014/07/RStudio-Logo-Blue-Gradient.png width = 400 height = 100 />

#Introduction to Computational Linguistics in R

[](https://www.rstudio.com/wp-content/uploads/2014/07/RStudio-Logo-Blue-Gradient.png)

R is a programming language designed particulary for use by statisticians and data scientists, but because of its vast library of packages it has uses that far surpass its original design.

A number of packages have been made in R for the specific purpose of Computational Linguistics, two of which we'll work with today in a brief demonstration.

*As a bit of a lengthy aside, I'd like to note that when approaching problems in Computational Linguistics and other fields, the specific programming language you use can matter either a lot or not at all. For example, just about everything that you can do in R can also do with Python, however the specific tool you want to use might only exist in one or other. In another case, the data you work with might be so large that you can't use either programming language in any efficient way. In summation, what's important when learning technical skills of this nature is not learning how to code, but how to approach a problem with what you do know and also to know when you need to learn new skills and techniques.*


## Installing R

The process for setting up R/RStudio is pretty straightforward, the individual installers should handle  everything with a minimum of issues. Just for clarification, R is the actual programming language, which when installed gives access to a very minimalistic command-line-esque terminal. RStudio, installed second, is an incredibly useful graphical interface which allows you to get more out of your workspace. *In short, I don't know anyone who programs in R and doesn't use RStudio or some variation thereof*

#### Step One

Download and install the R base [here](https://cran.r-project.org/)

#### Step Two

Download and install RStudio [here](https://www.rstudio.com/products/rstudio/download/)

## Tutorial Part The First

Today we'll be working with something that R is well sorted to dealing with, ngrams.

So what are ngrams? Well they're a type of language model based on the idea that you can retrieve meaningful information, namely the ability to product what word comes next, from only a small portion of text, the ngram. This is all a gross oversimplification of some pretty signicant statistics, but at the root is that idea that if I have the phrase...

* "What exactly does one do with an ngram?"

That I should be able to break that phrase into ngrams of size, say 3, like so...

* "What exactly does"
* "exactly does one"
* "does one do"
* "one do with"
* "do with an"
* "with an ngram?"

And assign some type of predictive value to each of those ngrams. For instance, I might say that the ngram "does one do" has a probabilistic value that the next word should be "with" of 20%. That of course is probably not accurate, but its just an example.

The actual methods used to extract information from ngrams become very complicated rather quickly, but there are also a number  of things that fairly easily.

<img src="http://betweenthenumbers.net/wp-content/uploads/2013/11/table-1.png">

#### Lets Make an Ngram

For this little tutorial I just grabbed a .txt version of the Project Gutenberg edition of Alice In Wonderland, but feel free to find your own bit of text to ngram-ize. Just make sure it ends in ".txt" and its a web source.

*Note: we won't be going into any in-depth look at R syntax today, if you want to learn more, there are resources at the end of this tutorial*

```r
  #The first step is to read the text file into R
  #This command opens the URL and defines each object by the whitespace around it
  data <- scan("http://www.textfiles.com/etext/FICTION/alice13a.txt",character(0))
  
  #You can look at what is now stored at x by typing
  #This prints all of the values stored in x
  x
  
  #If you only want to look at the beginning values, use the head() command
  head(x, 100)     # The "100" specifies to print the first 100 values of x
  
  #Or you can look at the end values, using the tail() command
  tail(x, 42) 
```

<img src="http://4.bp.blogspot.com/-IgIAqZffdFA/UMZ2rD_S98I/AAAAAAAAASk/qNnb-9EtKd4/s1600/google_book_ngram.png">

#### Google Ngrams viewer in R

On the extreme end of things, we have the Google Ngram Viewer, which has a corpus spanning 1800 to 2012 and sized up to 2.2 Terabytes of data. The resulting size tends to mean that only the most simple information can be extracted, beyond which any real study becomes increasingly complicated. 

You can experiment with the Google Ngram Viewer [here](https://books.google.com/ngrams)

At some point in time someone also adapted the Google Ngram Viewer to work in R, which we'll experiment with now.

```r

```


## For Those Interested In Learning More

#### The CRAN Library

CRAN, short for The Comprehensive R Network has a library containing thousands of packages which is update regularly. It happens to have several libraries of interest to computational linguistics of which the following are a few.

* More ngram tools with **ngramrr**, found [here](https://cran.r-project.org/web/packages/ngramrr/index.html) and [manual](https://cran.r-project.org/web/packages/ngramrr/ngramrr.pdf) here
* Natural Language Processing with **NLP**, found [here](https://cran.r-project.org/web/packages/NLPutils/index.html) with [manual](https://cran.r-project.org/web/packages/NLP/NLP.pdf) here
* Word Frequency Distributions **ZipfR**, found [here](https://cran.r-project.org/) with [manual](https://cran.r-project.org/web/packages/zipfR/zipfR.pdf) here

```r
#All packages can be installed using the following syntax
install.packages("package_name")
```

#### Tutorials

If you're interested in learning more about programming in R, Swirl tutorials can be downloaded and run directly in RStudio using the following commands.

```r
install.packages("swirl")
library(swirl)
swirl()
```
  
The full library of swirl courses is available [here](https://github.com/swirldev/swirl_courses)

#### Other Interesting Resources

Mostly just some things I stumbled across in the process of putting this all together




  


