# Lab 4

In this lab, we will get familiar with Weights & Biases, and start using an experiment-running framework that will make it easy to distribute work onto multiple GPUs.

## Weights & Biases

You'll notice some new lines in `training/run_experiment.py` now: importing and initializing `wandb`, the Weights & Biases package.

Because of this, you need to run  `wandb init`, where you can set your user id and create a new project.

Now let's test it out with a quick experiment: run `tasks/train_character_predictor.sh`

When it completes, you should see some new output from W&B, and a link to go check out the run.

Let's do that!

## Running multiple experiments

TODO
