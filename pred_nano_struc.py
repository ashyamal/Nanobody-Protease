from igfold import IgFoldRunner

nano_521_aa = "QVQLQESGGGLVQAGGSLTLSCAVSGLTFSNYAMGWFRQAPGKEREFVAAITWDGGNTYYTDSVKGRFTISRDNAKNTVFLQMNSLKPEDTAVYYCAAKLLGSSRYELALAGYDYWGQGTQVTVS"
nano_524_aa = "MGQVQLQESGGGLVQAGGSLRLSCVVSGTILSSNSMGWYRQAPGKRRELVASISTDGSTNYADSVKGRFTISRDNAKSTVFLQMNSLKPEDTAVYYCNFHPPVVRDWGDTYWGTQVTVSSAAAYPYDVPDYGGGGSGGGGSGGGGSLKEAKEKAIEELKKAGITSDYYFDLINKAKTVEGVNALKDEILKAGGGGSGGGGSGGGGSLKEAKEKAIEELKKAGITSDYYFDLINKAKTVEGVNALKDEILKAHHHHHHSPSTPPTPSPSTPPEEGEEGEEGEEGEEGEEGGC"

nano_seq = [('nano_521', nano_521_aa), ('nano_524', nano_524_aa)]

for s in nano_seq:
    sequences = {
        'H': s[1]
    }
    pred_pdb = s[0] + '.pdb'

    igfold = IgFoldRunner()
    igfold.fold(
        pred_pdb, # Output PDB file
        sequences=sequences, # Nanobody sequence
        do_refine=False, # Refine the antibody structure with PyRosetta
        do_renum=False, # Renumber predicted antibody structure (Chothia)
    )
