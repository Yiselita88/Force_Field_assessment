import MDAnalysis as mda
from MDAnalysis.analysis.dihedrals import Ramachandran
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Use the Agg backend for Matplotlib (does not require an interactive display)
plt.switch_backend('agg')

# Function to extract phi and psi from universe


def extract_angles(topology, trajectory):
    u = mda.Universe(topology, trajectory)
    r = u.select_atoms('backbone')

    # start and run Ramachandran
    R = Ramachandran(r).run()

    # extract angles from Ramachandran analysis
    phi_angles = R.angles[:, :, 0].flatten()  # Flat array for histogram
    psi_angles = R.angles[:, :, 1].flatten()

    return phi_angles, psi_angles


# Extract angles for each universe
phi1, psi1 = extract_angles("/orange/alberto.perezant/yisel/FF_assessment/FF/originals/AMBER/ff14IDPs/1GB1/analysis/mdanalysis_test/topol.top", "/orange/alberto.perezant/yisel/FF_assessment/FF/originals/AMBER/ff14IDPs/1GB1/analysis/mdanalysis_test/sieved_traj.dcd")
phi2, psi2 = extract_angles("/orange/alberto.perezant/yisel/FF_assessment/FF/originals/AMBER/ff14IDPsFF/1GB1/analysis/mdanalysis/topol.top", "/orange/alberto.perezant/yisel/FF_assessment/FF/originals/AMBER/ff14IDPsFF/1GB1/analysis/mdanalysis/sieved_traj.dcd")
phi3, psi3 = extract_angles("/orange/alberto.perezant/yisel/FF_assessment/FF/originals/AMBER/ff99sb/1GB1/analysis/mdanalysis/topol.top", "/orange/alberto.perezant/yisel/FF_assessment/FF/originals/AMBER/ff99sb/1GB1/analysis/mdanalysis/sieved_traj.dcd")
phi4, psi4 = extract_angles("/orange/alberto.perezant/yisel/FF_assessment/FF/originals/AMBER/ff99IDPs/1GB1/analysis/mdanalysis/topol.top", "/orange/alberto.perezant/yisel/FF_assessment/FF/originals/AMBER/ff99IDPs/1GB1/analysis/mdanalysis/sieved_traj.dcd")
phi5, psi5 = extract_angles("/orange/alberto.perezant/yisel/FF_assessment/FF/originals/AMBER/ff19sb/1GB1/analysis/mdanalysis/topol.top", "/orange/alberto.perezant/yisel/FF_assessment/FF/originals/AMBER/ff19sb/1GB1/analysis/mdanalysis/sieved_traj.dcd")
phi6, psi6 = extract_angles("/orange/alberto.perezant/yisel/FF_assessment/FF/originals/AMBER/charmm36m/1GB1/analysis/mdanalysis/topol.top", "/orange/alberto.perezant/yisel/FF_assessment/FF/originals/AMBER/charmm36m/1GB1/analysis/mdanalysis/sieved_traj.dcd")
phi7, psi7 = extract_angles("/orange/alberto.perezant/yisel/FF_assessment/FF/originals/GROMACS/a99SBdisp/1GB1/analysis/mdanalysis/topol.top", "/orange/alberto.perezant/yisel/FF_assessment/FF/originals/GROMACS/a99SBdisp/1GB1/analysis/mdanalysis/sieved_traj.dcd")
phi8, psi8 = extract_angles("/orange/alberto.perezant/yisel/FF_assessment/FF/originals/GROMACS/des-amber/1GB1/analysis/mdanalysis/topol.top", "/orange/alberto.perezant/yisel/FF_assessment/FF/originals/GROMACS/des-amber/1GB1/analysis/mdanalysis/sieved_traj.dcd")
phi9, psi9 = extract_angles("/orange/alberto.perezant/yisel/FF_assessment/FF/originals/GROMACS/des-amber-SF1.0/1GB1/analysis/mdanalysis/topol.top", "/orange/alberto.perezant/yisel/FF_assessment/FF/originals/GROMACS/des-amber-SF1.0/1GB1/analysis/mdanalysis/sieved_traj.dcd")
phi10, psi10 = extract_angles("/orange/alberto.perezant/yisel/FF_assessment/FF/originals/GROMACS/C36MIDPsFF/1GB1/analysis/mdanalysis/topol.top", "/orange/alberto.perezant/yisel/FF_assessment/FF/originals/GROMACS/C36MIDPsFF/1GB1/analysis/mdanalysis/sieved_traj.dcd")

# Create free energy landscapes


def create_free_energy(phi_angles, psi_angles):
    hist, xedges, yedges = np.histogram2d(phi_angles, psi_angles, bins=360, range=[[-180, 180], [-180, 180]], density=True)
    with np.errstate(divide='ignore'):
        free_energy = -np.log(hist)
        free_energy -= np.min(free_energy)
    free_energy = np.ma.masked_where(np.isinf(free_energy), free_energy)
    return free_energy


free_energy1 = create_free_energy(phi1, psi1)
free_energy2 = create_free_energy(phi2, psi2)
free_energy3 = create_free_energy(phi3, psi3)
free_energy4 = create_free_energy(phi4, psi4)
free_energy5 = create_free_energy(phi5, psi5)
free_energy6 = create_free_energy(phi6, psi6)
free_energy7 = create_free_energy(phi7, psi7)
free_energy8 = create_free_energy(phi8, psi8)
free_energy9 = create_free_energy(phi9, psi9)
free_energy10 = create_free_energy(phi10, psi10)

# Create a figure with GridSpec for tight layout control
fig = plt.figure(figsize=(15, 12))
gs = GridSpec(3, 4, hspace=0, wspace=0)
axs = [fig.add_subplot(gs[i]) for i in range(10)]

# Plotting function


def plot_free_energy(ax, free_energy, title, legend_label):
    im = ax.imshow(free_energy.T, origin='lower', extent=[-180, 180, -180, 180], cmap='Blues_r', aspect='auto')
    ax.set_title(title)
    ax.set_xlabel('Phi (°)')
    ax.set_ylabel('Psi (°)')
    ax.legend([legend_label], loc='upper right')
    return im


# Plot each free energy landscape
im1 = plot_free_energy(axs[0], free_energy1, 'ff14IDPs', 'ff14IDPs')
im2 = plot_free_energy(axs[1], free_energy2, 'ff14IDPsFF', 'ff14IDPsFF')
im3 = plot_free_energy(axs[2], free_energy3, 'ff99SB', 'ff99SB')
im4 = plot_free_energy(axs[3], free_energy4, 'ff99IDPs', 'ff99IDPs')
im5 = plot_free_energy(axs[4], free_energy5, 'ff19sb', 'ff19sb')
im6 = plot_free_energy(axs[5], free_energy6, 'charmm36m', 'charmm36m')
im7 = plot_free_energy(axs[6], free_energy7, 'a99SBdisp', 'a99SBdisp')
im8 = plot_free_energy(axs[7], free_energy8, 'des-amber', 'des-amber')
im9 = plot_free_energy(axs[8], free_energy9, 'des-amber-SF1.0', 'des-amber-SF1.0')
im10 = plot_free_energy(axs[9], free_energy10, 'C36MIDPsFF', 'C36MIDPsFF')

# Make outer labels visible
for ax in fig.get_axes():
    ax.label_outer()

# Create a single color bar outside the plot
# Adjust the position and size of the colorbar
cbar_ax = fig.add_axes([0.92, 0.15, 0.02, 0.7])
fig.colorbar(im4, cax=cbar_ax, label='Free Energy (kT)')

# Common labels
fig.text(0.5, 0.04, 'Phi (°)', ha='center', va='center')
fig.text(0.06, 0.5, 'Psi (°)', ha='center', va='center', rotation='vertical')

# Adjust layout
plt.tight_layout(rect=[0.06, 0.06, 0.9, 1])

# Save the figure with a transparent background
plt.savefig('mda_Ramachandran_all_original.png',transparent=True)

