from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO

record = SeqIO.read("Genome.gb", "genbank")

gd_diagram = GenomeDiagram.Diagram("Tomato curly stunt virus, complete genome.")
gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
gd_feature_set = gd_track_for_features.new_set()
lis = [colors.blue, colors.orange, colors.red, colors.black, colors.green]
i = 0

for feature in record.features:
    if feature.type != "gene":
        continue
    gd_feature_set.add_feature(
        feature, color=lis[i], label=True, label_size=24, label_angle=0
    )
    i+=1

gd_diagram.draw(
    format="circular",
    circular=True,
    pagesize=(20 * cm, 20 * cm),
    start=0,
    end=len(record),
    circle_core=0.8,
)

gd_diagram.write("plasmid_circular1.jpg", "JPG")
