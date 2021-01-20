# ACM Research Coding Challenge (Spring 2021)

## Explanation

The Library and Documentation I used at first was solely Biopython. However, after trying to find a better way to display the features I came across the DNA Features Viewer library. It accepts the genbank files given and assigns the color to the different genes in the diagram. It also labels the features names in order to show which gene is where on the strand. It also solves the problem of feature collision I was dealing with previously when using Biopython making the genome diagram look much nicer in the process. The only downside to this diagram is I was not able to change the colors when adding features when they are read from the genbank file, however you could allot specific colors to each feature if you did hardcode it.

## Future Improvements

This diagram could be improved by possibly using a scale within the diagram to show where on the strand the feature is exactly (in bp) and also maybe include different colors for each feature.

## Documentation for DNA Features Viewer

Source: https://github.com/Edinburgh-Genome-Foundry/DnaFeaturesViewer

Source: https://edinburgh-genome-foundry.github.io/DnaFeaturesViewer/

