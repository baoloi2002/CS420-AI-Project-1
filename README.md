# CS418-AI-Project-1

## Run main
The custom variables are in the square brackets (`[]`).
- `algo_module` is the file name of the module in `knapsack`, for example: `genetic`, `local_beam`, `genetic_0`. 
- `algoName` should be one of the created folder: `brute`, `branch`, `beam`, `genetic`.
- `X` is the test number.

For specific input and output file:
```
python main.py --algo [algo_module] test/input/INPUT_[X].txt test/output_[algoName]/OUTPUT_[X].txt
```
For input and output folder, this will use all files in the input folder: 
```
python main.py --algo [algo_module] --dir test/input test/output_[algoName]
```

## Validate output
Validate if the output is correct.
```
python validate.py test/input/INPUT_[X].txt test/output_[algoName]/OUTPUT_[X].txt
```