# Udacity Deep Reinforcement Learning Nanodegree Project 2: Continous Control

TBD

The steps below will describe how to get this running on MacOS:

## 1. Clone the repo

```
$ git clone https://github.com/aweeraman/reinforcement-learning-continuous-control.git
```

## 2. Install Python & dependencies

Using the Anaconda distribution, create a new python runtime and install the required dependencies:

```
$ conda create -n dqn python=3.6
$ source activate dqn
$ pip install -r requirements.txt
```

## 3. Install the Unity Environment

Download a pre-built environment to run the agent. You will not need to install Unity for this. The
environment is OS specific, so the correct version for the operating system must be downloaded.

For MacOS, [use this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher.app.zip)

After uncompressing, there should be a directory called "Reacher.app" in the root directory of the repository.

## 4. Run the agent

To run the pre-trained agent, execute the following:

```
$ python reacher.py --run
TBD
```

To customize hyperparameters and train the agent, execute the following:

```
$ python reacher.py --train
TBD
```

# Environment details

TBD

# Troubleshooting Tips

If you run into an error such as the following when training the agent:

```
ImportError: Python is not installed as a framework. The Mac OS X backend will not be able to function correctly if Python is not installed as a framework. See the Python documentation for more information on installing Python as a framework on Mac OS X. Please either reinstall Python as a framework, or try one of the other backends. If you are using (Ana)Conda please install python.app and replace the use of 'python' with 'pythonw'. See 'Working with Matplotlib on OSX' in the Matplotlib FAQ for more information.
```

Modify ~/.matplotlib/matplotlibrc and add the following line:

```
backend: TkAgg
```
