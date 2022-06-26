# Exercise 2
Hand in until **March 22nd at 23:59**.

## Introduction

This exercise is all about object-oriented programming (OOP), as you had it in the lectures. OOP allows you to use Python and your skills to a new extent. Once again, you will be working with dad jokes, but this time it is a csv-file. You will create classes and its methods to return jokes whenever you feel like being told a good ol' dad joke.

Please use modules from Python’s standard library only, unless it is stated otherwise in the exercise description.

### Unit Tests

Just like in the first exercise, you will need to write some more test assertions. Check corner cases and special cases, to see whether your code runs as it is supposed to.


### GitLab

To submit your code, use GitLab. Make sure your account is set up and ready to work with. Have a look at the instructions on ```OLAT > Material > Tutorial > instructions.pdf``` if you're unsure how to submit your work.


### To Submit

* Your UML diagram as a PDF
* Your answers for task 1 in the text file ```task_1.txt```
* Your implemented script ```processing.py```, including the new classes and methods
* Your feedback for this exercise in a text file ```feedback.txt```
* (Your answer file for the bonus task, ```bonus.txt```)


It is **mandatory** to work in pairs. If you have no partner, please contact us so we can set you up with someone. Before submitting, make sure all your code runs and your repository contains all the files you need to hand in.


## Task 1

Before working with real code, thinking in concepts is always helpful. We provided you with a sample script ```classes.py```. First of all, have a close look at the code and find out, what it does. If it helps, feel free to test it out as well. To get a good overview of the code, you create a [UML (Unified Modeling Language) diagram](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/) for it. This diagram helps to visualize inheritances, relations and attributes between the different blocks of code. Study the conventions of UML well and create your own diagram. You can draw it by hand or use an online tool like [Flowchart Maker and Online Diagram Software](https://app.diagrams.net). 

After your diagram is drawn, think of the following three cases and write the corresponding output to a text file ```task_1.txt```. Try answering without executing it in the code.

```python
# case 1
if __name__ == '__main__':
	dino = Velociraptor('Kara', 5)
	dino.roar()
	dino.nourish(5, 'water')
	dino.fight()
```

```python
# case 2
if __name__ == '__main__':
	dino = Dinosaur('Pepe', 1)
	dino.roar()
	dino.nourish(6)
```

```python
# case 3
if __name__ == '__main__':
	dino = Brachiosaurus('Sauri', 4)
	dino.mate()
	dino.roar()
	dino.fight()
```


### Outcome
* A PDF with your UML diagram for ```classes.py```
* A txt-file ```task_1.txt``` with your answers to the three cases


## Task 2

First of all, you will need to take the old code and rearrange it into the class ```Joke```. Have a look at the code skeleton ```processing.py``` we provided you with and fill in the missing methods. Think about which attributes and methods should be private or protected. This will prevent the user from (accidentally) messing with your code.

Furthermore, implement the function ```tell_joke() -> None```. The user should be able to call it and the joke should be returned in a manner, that there is a small build up. You can assume that the punchline is always the last sentence of the post. You can use ```time.sleep()``` to add a small waiting period (choose yourself how many seconds is best) before the punchline is revealed. The function should also return jokes that are only one sentence long.


### Outcome
* An implemented class ```Joke```
* An implemented function ```tell_joke() -> None```


## Task 3

Functional programming makes your coding experience even better. Python offers many so-called special methods which you can change as you like. For example, you can overwrite the ```print()``` function if you wish to change its return value. In this task, you will change two special methods. Firstly, change the special method ```__repr__``` so that it returns its argument how you implemented it in the ```pretty_print()``` function. Secondly, change the special methods of comparison, ```__eq__``` ```__lt__```, ```__gt__```, ```__le__``` and ```__ge__```, which are called when we compare two things, such as:

```python
10 == 2   # calls __eq__() internally 
```

Whenever two things are compared in your code, the scores of the jokes should be compared. The return value of the ```__eq__``` function should be the higher upvoted joke and its score.


### Outcome
* Your implementation for ```__repr__```
* Your implementation for ```__eq__```
* Your implementation for ```__lt__```
* Your implementation for ```__gt__```
* Your implementation for ```__le__```
* Your implementation for ```__ge__```

## Task 4

Next up, you will implement the second class given, ```JokeGenerator```. Implement the function ```make_jokes_objects()``` which reads the given file and stores all jokes as Joke-objects in a list. Use a list comprehension to do so. The second function ```generate_jokes()``` should take any joke and tell it, if it is longer than one sentence. To tell the joke, use the function you implemented before. The function ```random_joke()``` should return any random joke from the whole dataset and print it out nicely.


### Outcome
* An implemented class ```JokeGenerator```
* An implemented function ```make_jokes_objects```
* An implemented function ```generate_jokes()``` 
* An implemented function ```random_joke()``` 


## ✨ Bonus Task ✨

Can you write a small function to find the highest upvoted (= score) joke in our dataset. Include the function in your script and put the solution (joke and score) into a separate file ```bonus.txt``` 

### Outcome
* Implemented function in the script
* Your result in a separate text file ```bonus.txt```


## Feedback

Please give us a short feedback regarding this exercise.

a) How much time did you spend roughly on this exercise?

b) How difficult was this exercise? Was the difficulty too high, too low or just right?

c) Do you feel more comfortable now with the topics from the exercise and lectures?

### Outcome
* Your answers to a-c written in a separate text file named ```feedback.txt```.

## Data Sources
```dadjokes_samples.txt```: https://www.kaggle.com/oktayozturk010/reddit-dad-jokes

```profanities.txt```: https://www.freewebheaders.com/full-list-of-bad-words-banned-by-google/