# Example Pipeline

To run the example pipeline, simply go back to repo root directory and:

```shell
mv example_pipeline/dvc.yaml .
# activate your environment however you like
dvc init
dvc repro
```

You can see the pipeline run write it's data and metrics.

To see a nice diagram of the pipeline, run `dvc dag`.

Try modifying some stages and re-running the pipeline to get a sense of how dvc can help speed up your workflows. And once you've gotten some data on your disk, [setup a dvc remote cache](https://dvc.org/doc/user-guide/setup-google-drive-remote) to easily share intermediate data with your team.
