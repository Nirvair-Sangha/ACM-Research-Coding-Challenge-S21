from dna_features_viewer import BiopythonTranslator, CircularGraphicRecord
import matplotlib

matplotlib.rcParams['font.family'] = "Comic Sans MS"

class MyCustomTranslator(BiopythonTranslator):

    def compute_feature_color(self, feature):
        if feature.type == "CDS":
            return "turquoise"
        else:
            return "None"
            # return BiopythonTranslator.compute_feature_color(self, feature)
    
    def compute_feature_box_color(self, feature):
        return "lightcyan"

    def compute_feature_box_linewidth(self, feature):
        return 1

    def compute_feature_label_link_color(self, feature):
        return "indigo"

    def compute_filtered_features(self, features):
        return [
            feature for feature in features
            if (feature.type != "gene") and (feature.type != "source")
        ]
    
    def compute_feature_linewidth(self, feature):
        return 1.5
    
record = MyCustomTranslator().translate_record("Genome.gb", record_class=CircularGraphicRecord)

ax, b = record.plot(figure_width=5) # b has no real purpose

ax.figure.savefig("plasmid_circular.jpg")
