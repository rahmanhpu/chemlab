"""Test core types like Molecule and Atom.

"""
from chemlab import Molecule, Atom
from chemlab.core.system import SystemFast
from chemlab.core.spacegroup.crystal import crystal
import numpy as np
import unittest

def test_init():
    """Test initialization of the Molecule and Atom classes."""
    # Default units for coordinates are Angstroms
    
    mol = Molecule([Atom("O", [-4.99, 2.49, 0.0]),
                    Atom("H", [-4.02, 2.49, 0.0]),
                    Atom("H", [-5.32, 1.98, 1.0])],[])

def test_system():
    wat = Molecule([Atom("O", [-4.99, 2.49, 0.0]),
                    Atom("H", [-4.02, 2.49, 0.0]),
                    Atom("H", [-5.32, 1.98, 1.0])])

    wat.r_array *= 0.1
    s = SystemFast(4, 4*3)
    
    for i in xrange(s.n_mol):
        wat.r_array += 0.1
        s.add(wat)
    
    print s.r_array
    print s.m_array
    print s.type_array
    print s.mol_indices
    print s.mol_n_atoms

    print 'This an array with all center of masses'
    print s.get_derived_molecule_array('center_of_mass')
    print 'Test Indexing'
    print s.molecules[0]
    print s.molecules[:], s.molecules[:-5]

    print s.atoms[0]
    print s.atoms[:]

def test_crystal():
    '''Building a crystal by using spacegroup module'''
    na = Molecule([Atom('Na', [0.0, 0.0, 0.0])])
    cl = Molecule([Atom('Cl', [0.0, 0.0, 0.0])])
    
    # Fract position of Na and Cl, space group 255
    tsys = crystal([[0.0, 0.0, 0.0],[0.5, 0.5, 0.5]], [na, cl], 225, repetitions=[13,13,13])
    
    
        