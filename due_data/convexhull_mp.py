from pymatgen.ext.matproj import MPRester
from pymatgen.analysis.phase_diagram import PhaseDiagram, PDPlotter, PDEntry
from pymatgen.core.composition import Composition
from itertools import combinations
API_KEY = 'DPYgIrbjIbcLENX7sYIRn5Qi5GD8c47Z'
new_formula = 'Cs4Pb4Br12'
new_energy = -3.53387 

elements = [element.symbol for element in Composition(new_formula)]
with MPRester(API_KEY) as mpr:
    entries = []
    for i in range(1, len(elements) + 1):
        for subset in combinations(elements, i):
            entries += mpr.get_entries_in_chemsys(list(subset))

new_entry = PDEntry(composition=Composition(new_formula), energy=new_energy)
entries.append(new_entry)
pd = PhaseDiagram(entries)
e_above_hull_new = pd.get_e_above_hull(new_entry)

print(f'The e_above_hull for the new structure {new_formula} is {e_above_hull_new:.4f} eV')
plotter = PDPlotter(pd)
plotter.show()
