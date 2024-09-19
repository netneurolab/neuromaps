.. _listofmaps:

------------
List of Maps
------------
This is a complete list of maps available in the `neuromaps` package. 

----

abagen-genepc1-fsaverage-10k
============================

**Annotation identifier**

*{'source': 'abagen', 'desc': 'genepc1', 'space': 'fsaverage', 'den': '10k'}*

**Full description**

PC1 of genes in the Allen Human Brain Atlas

**Demographics**: N = 6, Age = 24-55

**Tags**: genetics

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='abagen', desc='genepc1', space='fsaverage', den='10k')

    # describe annotation
    describe_annotations(('abagen', 'genepc1', 'fsaverage', '10k'))

    # file location
    # $NEUROMAPS_DATA/abagen/genepc1/fsaverage/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-abagen_desc-genepc1_space-fsaverage_den-10k_hemi-L_feature.func.gii

**References**
    - Michael J Hawrylycz, Ed S Lein, Angela L Guillozet-Bongaarts, Elaine H Shen, Lydia Ng, Jeremy A Miller, Louie N Van De Lagemaat, Kimberly A Smith, Amanda Ebbert, Zackery L Riley, and others. An anatomically comprehensive atlas of the adult human brain transcriptome. Nature, 489(7416):391, 2012.
    - Ross D Markello, Aurina Arnatkeviciute, Jean-Baptiste Poline, Ben D Fulcher, Alex Fornito, and Bratislav Misic. Standardizing workflows in imaging transcriptomics with the abagen toolbox. eLife, 10:e72129, 2021.

----

aghourian2017-feobv-MNI152-1mm
==============================

**Annotation identifier**

*{'source': 'aghourian2017', 'desc': 'feobv', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (SUVR) to VAChT (acetylcholine transporter)

**Demographics**: N = 18, Age = 66.8 +/- 6.8

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='aghourian2017', desc='feobv', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('aghourian2017', 'feobv', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/aghourian2017/feobv/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-aghourian2017_desc-feobv_space-MNI152_res-1mm_feature.nii.gz

**References**
    - M Aghourian, C Legault-Denis, JP Soucy, P Rosa-Neto, S Gauthier, A Kostikov, P Gravel, and MA Bedard. Quantification of brain cholinergic denervation in alzheimer’s disease using pet imaging with [18 f]-feobv. Molecular psychiatry, 22(11):1531–1538, 2017.
    - Justine Y Hansen, Golia Shafiei, Ross D Markello, Kelly Smart, Sylvia ML Cox, Martin Nørgaard, Vincent Beliveau, Yanjun Wu, Jean-Dominique Gallezot, Étienne Aumont, and others. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. Nature neuroscience, 25(11):1569–1581, 2022.

----

alarkurtti2015-raclopride-MNI152-3mm
====================================

**Annotation identifier**

*{'source': 'alarkurtti2015', 'desc': 'raclopride', 'space': 'MNI152', 'res': '3mm'}*

**Full description**

PET tracer binding (BPnd) to D2 (dopamine receptor)

**Demographics**: N = 7, Age = 24 +/- 2

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='alarkurtti2015', desc='raclopride', space='MNI152', res='3mm')

    # describe annotation
    describe_annotations(('alarkurtti2015', 'raclopride', 'MNI152', '3mm'))

    # file location
    # $NEUROMAPS_DATA/alarkurtti2015/raclopride/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-alarkurtti2015_desc-raclopride_space-MNI152_res-3mm_feature.nii.gz

**References**
    - Kati Alakurtti, Jarkko J Johansson, Juho Joutsa, Matti Laine, Lars Bäckman, Lars Nyberg, and Juha O Rinne. Long-term test–retest reliability of striatal and extrastriatal dopamine d2/3 receptor binding: study with [11c] raclopride and high-resolution pet. Journal of Cerebral Blood Flow & Metabolism, 35(7):1199–1205, 2015.

----

bedard2019-feobv-MNI152-1mm
===========================

**Annotation identifier**

*{'source': 'bedard2019', 'desc': 'feobv', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (SUVR) to VAChT (acetylcholine transporter)

**Demographics**: N = 5, Age = 68.3 +/- 3.1

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='bedard2019', desc='feobv', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('bedard2019', 'feobv', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/bedard2019/feobv/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-bedard2019_desc-feobv_space-MNI152_res-1mm_feature.nii.gz

**References**
    - Marc-Andre Bedard, Meghmik Aghourian, Camille Legault-Denis, Ronald B Postuma, Jean-Paul Soucy, Jean-François Gagnon, Amélie Pelletier, and Jacques Montplaisir. Brain cholinergic alterations in idiopathic rem sleep behaviour disorder: a pet imaging study with 18f-feobv. Sleep medicine, 58:35–41, 2019.
    - Justine Y Hansen, Golia Shafiei, Ross D Markello, Kelly Smart, Sylvia ML Cox, Martin Nørgaard, Vincent Beliveau, Yanjun Wu, Jean-Dominique Gallezot, Étienne Aumont, and others. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. Nature neuroscience, 25(11):1569–1581, 2022.

----

beliveau2017-az10419369-MNI152-1mm
==================================

**Annotation identifier**

*{'source': 'beliveau2017', 'desc': 'az10419369', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (Bmax) to 5-HT1b (serotonin receptor)

**Demographics**: N = 36, Age = 27.8 +/- 6.9

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='beliveau2017', desc='az10419369', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('beliveau2017', 'az10419369', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/beliveau2017/az10419369/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-beliveau2017_desc-az10419369_space-MNI152_res-1mm_feature.nii.gz

**Warning**

This annotation is best used in the provided fsaverage space. MNI152 maps should only be used for subcortical data.

**References**
    - Vincent Beliveau, Melanie Ganz, Ling Feng, Brice Ozenne, Liselotte Højgaard, Patrick M Fisher, Claus Svarer, Douglas N Greve, and Gitte M Knudsen. A high-resolution in vivo atlas of the human brain's serotonin system. Journal of Neuroscience, 37(1):120–128, 2017.

----

beliveau2017-az10419369-fsaverage-164k
======================================

**Annotation identifier**

*{'source': 'beliveau2017', 'desc': 'az10419369', 'space': 'fsaverage', 'den': '164k'}*

**Full description**

PET tracer binding (Bmax) to 5-HT1b (serotonin receptor)

**Demographics**: N = 36, Age = 27.8 +/- 6.9

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='beliveau2017', desc='az10419369', space='fsaverage', den='164k')

    # describe annotation
    describe_annotations(('beliveau2017', 'az10419369', 'fsaverage', '164k'))

    # file location
    # $NEUROMAPS_DATA/beliveau2017/az10419369/fsaverage/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-beliveau2017_desc-az10419369_space-fsaverage_den-164k_hemi-L_feature.func.gii

**References**
    - Vincent Beliveau, Melanie Ganz, Ling Feng, Brice Ozenne, Liselotte Højgaard, Patrick M Fisher, Claus Svarer, Douglas N Greve, and Gitte M Knudsen. A high-resolution in vivo atlas of the human brain's serotonin system. Journal of Neuroscience, 37(1):120–128, 2017.

----

beliveau2017-cimbi36-MNI152-1mm
===============================

**Annotation identifier**

*{'source': 'beliveau2017', 'desc': 'cimbi36', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (Bmax) to 5-HT2a (serotonin receptor)

**Demographics**: N = 29, Age = 22.6 +/- 2.7

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='beliveau2017', desc='cimbi36', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('beliveau2017', 'cimbi36', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/beliveau2017/cimbi36/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-beliveau2017_desc-cimbi36_space-MNI152_res-1mm_feature.nii.gz

**Warning**

This annotation is best used in the provided fsaverage space. MNI152 maps should only be used for subcortical data.

**References**
    - Vincent Beliveau, Melanie Ganz, Ling Feng, Brice Ozenne, Liselotte Højgaard, Patrick M Fisher, Claus Svarer, Douglas N Greve, and Gitte M Knudsen. A high-resolution in vivo atlas of the human brain's serotonin system. Journal of Neuroscience, 37(1):120–128, 2017.

----

beliveau2017-cimbi36-fsaverage-164k
===================================

**Annotation identifier**

*{'source': 'beliveau2017', 'desc': 'cimbi36', 'space': 'fsaverage', 'den': '164k'}*

**Full description**

PET tracer binding (Bmax) to 5-HT2a (serotonin receptor)

**Demographics**: N = 29, Age = 22.6 +/- 2.7

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='beliveau2017', desc='cimbi36', space='fsaverage', den='164k')

    # describe annotation
    describe_annotations(('beliveau2017', 'cimbi36', 'fsaverage', '164k'))

    # file location
    # $NEUROMAPS_DATA/beliveau2017/cimbi36/fsaverage/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-beliveau2017_desc-cimbi36_space-fsaverage_den-164k_hemi-L_feature.func.gii

**References**
    - Vincent Beliveau, Melanie Ganz, Ling Feng, Brice Ozenne, Liselotte Højgaard, Patrick M Fisher, Claus Svarer, Douglas N Greve, and Gitte M Knudsen. A high-resolution in vivo atlas of the human brain's serotonin system. Journal of Neuroscience, 37(1):120–128, 2017.

----

beliveau2017-cumi101-MNI152-1mm
===============================

**Annotation identifier**

*{'source': 'beliveau2017', 'desc': 'cumi101', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (Bmax) to 5-HT1a (serotonin receptor)

**Demographics**: N = 8, Age = 28.4 +/- 8.8

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='beliveau2017', desc='cumi101', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('beliveau2017', 'cumi101', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/beliveau2017/cumi101/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-beliveau2017_desc-cumi101_space-MNI152_res-1mm_feature.nii.gz

**Warning**

This annotation is best used in the provided fsaverage space. MNI152 maps should only be used for subcortical data.

**References**
    - Vincent Beliveau, Melanie Ganz, Ling Feng, Brice Ozenne, Liselotte Højgaard, Patrick M Fisher, Claus Svarer, Douglas N Greve, and Gitte M Knudsen. A high-resolution in vivo atlas of the human brain's serotonin system. Journal of Neuroscience, 37(1):120–128, 2017.

----

beliveau2017-cumi101-fsaverage-164k
===================================

**Annotation identifier**

*{'source': 'beliveau2017', 'desc': 'cumi101', 'space': 'fsaverage', 'den': '164k'}*

**Full description**

PET tracer binding (Bmax) to 5-HT1a (serotonin receptor)

**Demographics**: N = 8, Age = 28.4 +/- 8.8

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='beliveau2017', desc='cumi101', space='fsaverage', den='164k')

    # describe annotation
    describe_annotations(('beliveau2017', 'cumi101', 'fsaverage', '164k'))

    # file location
    # $NEUROMAPS_DATA/beliveau2017/cumi101/fsaverage/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-beliveau2017_desc-cumi101_space-fsaverage_den-164k_hemi-L_feature.func.gii

**References**
    - Vincent Beliveau, Melanie Ganz, Ling Feng, Brice Ozenne, Liselotte Højgaard, Patrick M Fisher, Claus Svarer, Douglas N Greve, and Gitte M Knudsen. A high-resolution in vivo atlas of the human brain's serotonin system. Journal of Neuroscience, 37(1):120–128, 2017.

----

beliveau2017-dasb-MNI152-1mm
============================

**Annotation identifier**

*{'source': 'beliveau2017', 'desc': 'dasb', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (Bmax) to 5-HTT (serotonin transporter)

**Demographics**: N = 100, Age = 25.1 +/- 5.8

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='beliveau2017', desc='dasb', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('beliveau2017', 'dasb', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/beliveau2017/dasb/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-beliveau2017_desc-dasb_space-MNI152_res-1mm_feature.nii.gz

**Warning**

This annotation is best used in the provided fsaverage space. MNI152 maps should only be used for subcortical data.

**References**
    - Vincent Beliveau, Melanie Ganz, Ling Feng, Brice Ozenne, Liselotte Højgaard, Patrick M Fisher, Claus Svarer, Douglas N Greve, and Gitte M Knudsen. A high-resolution in vivo atlas of the human brain's serotonin system. Journal of Neuroscience, 37(1):120–128, 2017.

----

beliveau2017-dasb-fsaverage-164k
================================

**Annotation identifier**

*{'source': 'beliveau2017', 'desc': 'dasb', 'space': 'fsaverage', 'den': '164k'}*

**Full description**

PET tracer binding (Bmax) to 5-HTT (serotonin transporter)

**Demographics**: N = 100, Age = 25.1 +/- 5.8

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='beliveau2017', desc='dasb', space='fsaverage', den='164k')

    # describe annotation
    describe_annotations(('beliveau2017', 'dasb', 'fsaverage', '164k'))

    # file location
    # $NEUROMAPS_DATA/beliveau2017/dasb/fsaverage/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-beliveau2017_desc-dasb_space-fsaverage_den-164k_hemi-L_feature.func.gii

**References**
    - Vincent Beliveau, Melanie Ganz, Ling Feng, Brice Ozenne, Liselotte Højgaard, Patrick M Fisher, Claus Svarer, Douglas N Greve, and Gitte M Knudsen. A high-resolution in vivo atlas of the human brain's serotonin system. Journal of Neuroscience, 37(1):120–128, 2017.

----

beliveau2017-sb207145-MNI152-1mm
================================

**Annotation identifier**

*{'source': 'beliveau2017', 'desc': 'sb207145', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (Bmax) to 5-HT4 (serotonin receptor)

**Demographics**: N = 59, Age = 25.9 +/- 5.3

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='beliveau2017', desc='sb207145', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('beliveau2017', 'sb207145', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/beliveau2017/sb207145/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-beliveau2017_desc-sb207145_space-MNI152_res-1mm_feature.nii.gz

**Warning**

This annotation is best used in the provided fsaverage space. MNI152 maps should only be used for subcortical data.

**References**
    - Vincent Beliveau, Melanie Ganz, Ling Feng, Brice Ozenne, Liselotte Højgaard, Patrick M Fisher, Claus Svarer, Douglas N Greve, and Gitte M Knudsen. A high-resolution in vivo atlas of the human brain's serotonin system. Journal of Neuroscience, 37(1):120–128, 2017.

----

beliveau2017-sb207145-fsaverage-164k
====================================

**Annotation identifier**

*{'source': 'beliveau2017', 'desc': 'sb207145', 'space': 'fsaverage', 'den': '164k'}*

**Full description**

PET tracer binding (Bmax) to 5-HT4 (serotonin receptor)

**Demographics**: N = 59, Age = 25.9 +/- 5.3

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='beliveau2017', desc='sb207145', space='fsaverage', den='164k')

    # describe annotation
    describe_annotations(('beliveau2017', 'sb207145', 'fsaverage', '164k'))

    # file location
    # $NEUROMAPS_DATA/beliveau2017/sb207145/fsaverage/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-beliveau2017_desc-sb207145_space-fsaverage_den-164k_hemi-L_feature.func.gii

**References**
    - Vincent Beliveau, Melanie Ganz, Ling Feng, Brice Ozenne, Liselotte Højgaard, Patrick M Fisher, Claus Svarer, Douglas N Greve, and Gitte M Knudsen. A high-resolution in vivo atlas of the human brain's serotonin system. Journal of Neuroscience, 37(1):120–128, 2017.

----

castrillon2023-cmrglc-MNI152-3mm
================================

**Annotation identifier**

*{'source': 'castrillon2023', 'desc': 'cmrglc', 'space': 'MNI152', 'res': '3mm'}*

**Full description**

Glucose metabolism

**Demographics**: N = None, Age = None

**Tags**: functional, PET, metabolism, resteyesopen

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='castrillon2023', desc='cmrglc', space='MNI152', res='3mm')

    # describe annotation
    describe_annotations(('castrillon2023', 'cmrglc', 'MNI152', '3mm'))

    # file location
    # $NEUROMAPS_DATA/castrillon2023/cmrglc/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-castrillon2023_desc-cmrglc_space-MNI152_res-3mm_feature.nii.gz

**References**
    - Gabriel Castrillon, Samira Epp, Antonia Bose, Laura Fraticelli, André Hechler, Roman Belenya, Andreas Ranft, Igor Yakushev, Lukas Utz, Lalith Sundar, and others. An energy costly architecture of neuromodulators for human brain evolution and cognition. Science advances, 9(50):eadi7632, 2023.

----

ding2010-mrb-MNI152-1mm
=======================

**Annotation identifier**

*{'source': 'ding2010', 'desc': 'mrb', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (BPnd) to NET (norepinephrine transporter)

**Demographics**: N = 77, Age = 33.4 +/- 9.17

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='ding2010', desc='mrb', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('ding2010', 'mrb', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/ding2010/mrb/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-ding2010_desc-mrb_space-MNI152_res-1mm_feature.nii.gz

**References**
    - Yu-Shin Ding, Tarun Singhal, Beata Planeta-Wilson, Jean-Dominique Gallezot, Nabeel Nabulsi, David Labaree, Jim Ropchan, Shannan Henry, Wendol Williams, Richard E Carson, and others. Pet imaging of the effects of age and cocaine on the norepinephrine transporter in the human brain using (s, s)-[11c] o-methylreboxetine and hrrt. Synapse, 64(1):30–38, 2010.
    - Justine Y Hansen, Golia Shafiei, Ross D Markello, Kelly Smart, Sylvia ML Cox, Martin Nørgaard, Vincent Beliveau, Yanjun Wu, Jean-Dominique Gallezot, Étienne Aumont, and others. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. Nature neuroscience, 25(11):1569–1581, 2022.
    - R Li Chiang-shan, Marc N Potenza, Dianne E Lee, Beata Planeta, Jean-Dominique Gallezot, David Labaree, Shannan Henry, Nabeel Nabulsi, Rajita Sinha, Yu-Shin Ding, and others. Decreased norepinephrine transporter availability in obesity: positron emission tomography imaging with (s, s)-[11c] o-methylreboxetine. Neuroimage, 86:306–310, 2014.
    - Elizabeth Sanchez-Rangel, Jean-Dominique Gallezot, Catherine W Yeckel, Wai Lam, Renata Belfort-DeAguiar, Ming-Kai Chen, Richard E Carson, Robert Sherwin, and Janice J Hwang. Norepinephrine transporter availability in brown fat is reduced in obesity: a human pet study with [11 c] mrb. International Journal of Obesity, 44(4):964–967, 2020.
    - Renata Belfort-DeAguiar, Jean-Dominique Gallezot, Janice J Hwang, Ahmed Elshafie, Catherine W Yeckel, Owen Chan, Richard E Carson, Yu-Shin Ding, and Robert S Sherwin. Noradrenergic activity in the human brain: a mechanism supporting the defense against hypoglycemia. The Journal of Clinical Endocrinology & Metabolism, 103(6):2244–2252, 2018.

----

dubois2015-abp688-MNI152-1mm
============================

**Annotation identifier**

*{'source': 'dubois2015', 'desc': 'abp688', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (BPnd) to mGluR5 (glutamate receptor)

**Demographics**: N = 28, Age = 33.1 +/- 11.2

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='dubois2015', desc='abp688', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('dubois2015', 'abp688', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/dubois2015/abp688/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-dubois2015_desc-abp688_space-MNI152_res-1mm_feature.nii.gz

**References**
    - Jonathan M DuBois, Olivier G Rousset, Jared Rowley, Manuel Porras-Betancourt, Andrew J Reader, Aurelie Labbe, Gassan Massarweh, Jean-Paul Soucy, Pedro Rosa-Neto, and Eliane Kobayashi. Characterization of age/sex and the regional distribution of mglur5 availability in the healthy human brain measured by high-resolution [11 c] abp688 pet. European journal of nuclear medicine and molecular imaging, 43(1):152–162, 2016.
    - Justine Y Hansen, Golia Shafiei, Ross D Markello, Kelly Smart, Sylvia ML Cox, Martin Nørgaard, Vincent Beliveau, Yanjun Wu, Jean-Dominique Gallezot, Étienne Aumont, and others. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. Nature neuroscience, 25(11):1569–1581, 2022.

----

dukart2018-flumazenil-MNI152-3mm
================================

**Annotation identifier**

*{'source': 'dukart2018', 'desc': 'flumazenil', 'space': 'MNI152', 'res': '3mm'}*

**Full description**

PET tracer binding (BPnd) to GABAa (gaba receptor)

**Demographics**: N = 6, Age = 43 +/- 4

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='dukart2018', desc='flumazenil', space='MNI152', res='3mm')

    # describe annotation
    describe_annotations(('dukart2018', 'flumazenil', 'MNI152', '3mm'))

    # file location
    # $NEUROMAPS_DATA/dukart2018/flumazenil/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-dukart2018_desc-flumazenil_space-MNI152_res-3mm_feature.nii.gz

**References**
    - Juergen Dukart, Štefan Holiga, Christopher Chatham, Peter Hawkins, Anna Forsyth, Rebecca McMillan, Jim Myers, Anne R Lingford-Hughes, David J Nutt, Emilio Merlo-Pich, and others. Cerebral blood flow predicts differential neurotransmitter activity. Scientific reports, 8(1):1–11, 2018.

----

dukart2018-fpcit-MNI152-3mm
===========================

**Annotation identifier**

*{'source': 'dukart2018', 'desc': 'fpcit', 'space': 'MNI152', 'res': '3mm'}*

**Full description**

SPECT tracer binding (SUVR) to DAT (dopamine transporter)

**Demographics**: N = 174, Age = 61 +/- 11

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='dukart2018', desc='fpcit', space='MNI152', res='3mm')

    # describe annotation
    describe_annotations(('dukart2018', 'fpcit', 'MNI152', '3mm'))

    # file location
    # $NEUROMAPS_DATA/dukart2018/fpcit/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-dukart2018_desc-fpcit_space-MNI152_res-3mm_feature.nii.gz

**References**
    - Juergen Dukart, Štefan Holiga, Christopher Chatham, Peter Hawkins, Anna Forsyth, Rebecca McMillan, Jim Myers, Anne R Lingford-Hughes, David J Nutt, Emilio Merlo-Pich, and others. Cerebral blood flow predicts differential neurotransmitter activity. Scientific reports, 8(1):1–11, 2018.

----

fazio2016-madam-MNI152-3mm
==========================

**Annotation identifier**

*{'source': 'fazio2016', 'desc': 'madam', 'space': 'MNI152', 'res': '3mm'}*

**Full description**

PET tracer binding (BPnd) to 5-HTT (serotonin transporter)

**Demographics**: N = 10, Age = 51-67

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='fazio2016', desc='madam', space='MNI152', res='3mm')

    # describe annotation
    describe_annotations(('fazio2016', 'madam', 'MNI152', '3mm'))

    # file location
    # $NEUROMAPS_DATA/fazio2016/madam/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-fazio2016_desc-madam_space-MNI152_res-3mm_feature.nii.gz

**References**
    - Patrik Fazio, Martin Schain, Katarina Varnäs, Christer Halldin, Lars Farde, and Andrea Varrone. Mapping the distribution of serotonin transporter in the human brainstem with high-resolution pet: validation using postmortem autoradiography data. Neuroimage, 133:313–320, 2016.

----

finnema2016-ucbj-MNI152-1mm
===========================

**Annotation identifier**

*{'source': 'finnema2016', 'desc': 'ucbj', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (BPnd) to SV2A (synaptic vesicle glycoprotein 2A, a synapse marker)

**Demographics**: N = 76, Age = 48.9 +/- 18.4

**Tags**: PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='finnema2016', desc='ucbj', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('finnema2016', 'ucbj', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/finnema2016/ucbj/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-finnema2016_desc-ucbj_space-MNI152_res-1mm_feature.nii.gz

**References**
    - Sjoerd J Finnema, Nabeel B Nabulsi, Joël Mercier, Shu-fei Lin, Ming-Kai Chen, David Matuskey, Jean-Dominique Gallezot, Shannan Henry, Jonas Hannestad, Yiyun Huang, and others. Kinetic evaluation and test–retest reproducibility of [11c] ucb-j, a novel radioligand for positron emission tomography imaging of synaptic vesicle glycoprotein 2a in humans. Journal of Cerebral Blood Flow & Metabolism, 38(11):2041–2052, 2018.
    - Mika Naganawa, Nabeel Nabulsi, Shannan Henry, David Matuskey, Shu-Fei Lin, Lawrence Slieker, Adam J Schwarz, Nancy Kant, Cynthia Jesudason, Kevin Ruley, and others. First-in-human assessment of 11c-lsn3172176, an m1 muscarinic acetylcholine receptor pet radiotracer. Journal of Nuclear Medicine, 62(4):553–560, 2021.
    - Justine Y Hansen, Golia Shafiei, Jacob W Vogel, Kelly Smart, Carrie E Bearden, Martine Hoogman, Barbara Franke, Daan Van Rooij, Jan Buitelaar, Carrie R McDonald, and others. Local molecular and global connectomic contributions to cross-disorder cortical abnormalities. Nature communications, 13(1):1–17, 2022.
    - Ming-Kai Chen, Adam P Mecca, Mika Naganawa, Jean-Dominique Gallezot, Takuya Toyonaga, Jayanta Mondal, Sjoerd J Finnema, Shu-fei Lin, Ryan S O’Dell, Julia W McDonald, and others. Comparison of [11c] ucb-j and [18f] fdg pet in alzheimer’s disease: a tracer kinetic modeling study. Journal of Cerebral Blood Flow & Metabolism, pages 0271678X211004312, 2021.
    - Ryan S O’Dell, Adam P Mecca, Ming-Kai Chen, Mika Naganawa, Takuya Toyonaga, Yihuan Lu, Tyler A Godek, Joanna E Harris, Hugh H Bartlett, Emmie R Banks, and others. Association of aβ deposition and regional synaptic density in early alzheimer’s disease: a pet imaging study with [11 c] ucb-j. Alzheimer's Research & Therapy, 13(1):1–12, 2021.
    - Kelly Smart, Heather Liu, David Matuskey, Ming-Kai Chen, Kristen Torres, Nabeel Nabulsi, David Labaree, Jim Ropchan, Ansel T Hillmer, Yiyun Huang, and others. Binding of the synaptic vesicle radiotracer [11c] ucb-j is unchanged during functional brain activation using a visual stimulation task. Journal of Cerebral Blood Flow & Metabolism, 41(5):1067–1079, 2021.
    - Julian J Weiss, Rachela Calvi, Mika Naganawa, Takuya Toyonaga, Shelli F Farhadian, Michelle Chintanaphol, Jennifer Chiarelle, Ming-Qiang Zheng, Jim Ropchan, Yiyun Huang, Robert H Pietrzak, Richard E Carson, and Serena Spudich. Preliminary in vivo evidence of reduced synaptic density in human immunodeficiency virus (hiv) despite antiretroviral therapy. Clinical Infectious Diseases, 73(8):1404–1411, 2021.
    - Rajiv Radhakrishnan, Patrick D Skosnik, Mohini Ranganathan, Mika Naganawa, Takuya Toyonaga, Sjoerd Finnema, Ansel T Hillmer, Irina Esterlis, Yiyun Huang, Nabeel Nabulsi, and others. In vivo evidence of lower synaptic vesicle density in schizophrenia. Molecular Psychiatry, pages 1–9, 2021.
    - Deepak Cyril D’Souza, Jose A Cortes-Briones, Mohini Ranganathan, Halle Thurnauer, Gina Creatura, Toral Surti, Beata Planeta, Alexander Neumeister, Brian Pittman, Marc D Normandin, and others. Rapid changes in cannabinoid 1 receptor availability in cannabis-dependent male subjects after abstinence from cannabis. Biological psychiatry: cognitive neuroscience and neuroimaging, 1(1):60–67, 2016.
    - Sjoerd J Finnema, Takuya Toyonaga, Kamil Detyniecki, Ming-Kai Chen, Mark Dias, Qianyu Wang, Shu-Fei Lin, Mika Naganawa, Jean-Dominique Gallezot, Yihuan Lu, and others. Reduced synaptic vesicle protein 2a binding in temporal lobe epilepsy: a [11c] ucb-j positron emission tomography study. Epilepsia, 61(10):2183–2193, 2020.
    - Jason Bini, Daniel Holden, Kathryn Fontaine, Tim Mulnix, Yihuan Lu, David Matuskey, Jim Ropchan, Nabeel Nabulsi, Yiyun Huang, and Richard E Carson. Human adult and adolescent biodistribution and dosimetry of the synaptic vesicle glycoprotein 2a radioligand 11 c-ucb-j. EJNMMI research, 10(1):1–8, 2020.
    - Adam P Mecca, Ming-Kai Chen, Ryan S O'Dell, Mika Naganawa, Takuya Toyonaga, Tyler A Godek, Joanna E Harris, Hugh H Bartlett, Wenzhen Zhao, Nabeel B Nabulsi, and others. In vivo measurement of widespread synaptic loss in alzheimer's disease with sv2a pet. Alzheimer's & Dementia, 16(7):974–982, 2020.
    - Sjoerd J Finnema, Samantha Rossano, Mika Naganawa, Shannan Henry, Hong Gao, Richard Pracitto, Ralph P Maguire, Joël Mercier, Sophie Kervyn, Jean-Marie Nicolas, and others. A single-center, open-label positron emission tomography study to evaluate brivaracetam and levetiracetam synaptic vesicle glycoprotein 2a binding in healthy volunteers. Epilepsia, 60(5):958–967, 2019.
    - Sophie E Holmes, Dustin Scheinost, Sjoerd J Finnema, Mika Naganawa, Margaret T Davis, Nicole DellaGioia, Nabeel Nabulsi, David Matuskey, Gustavo A Angarita, Robert H Pietrzak, and others. Lower synaptic density is associated with depression severity and network alterations. Nature communications, 10(1):1–10, 2019.
    - Ming-Kai Chen, Adam P Mecca, Mika Naganawa, Sjoerd J Finnema, Takuya Toyonaga, Shu-fei Lin, Soheila Najafzadeh, Jim Ropchan, Yihuan Lu, Julia W McDonald, and others. Assessing synaptic density in alzheimer disease with synaptic vesicle glycoprotein 2a positron emission tomographic imaging. JAMA neurology, 75(10):1215–1224, 2018.

----

gallezot2010-p943-MNI152-1mm
============================

**Annotation identifier**

*{'source': 'gallezot2010', 'desc': 'p943', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (BPnd) to 5-HT1b (serotonin receptor)

**Demographics**: N = 23, Age = 28.7 +/- 7

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='gallezot2010', desc='p943', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('gallezot2010', 'p943', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/gallezot2010/p943/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-gallezot2010_desc-p943_space-MNI152_res-1mm_feature.nii.gz

**References**
    - Jean-Dominique Gallezot, Nabeel Nabulsi, Alexander Neumeister, Beata Planeta-Wilson, Wendol A Williams, Tarun Singhal, Sunhee Kim, R Paul Maguire, Timothy McCarthy, J James Frost, and others. Kinetic modeling of the serotonin 5-ht1b receptor radioligand [11c] p943 in humans. Journal of Cerebral Blood Flow & Metabolism, 30(1):196–210, 2010.
    - Justine Y Hansen, Golia Shafiei, Ross D Markello, Kelly Smart, Sylvia ML Cox, Martin Nørgaard, Vincent Beliveau, Yanjun Wu, Jean-Dominique Gallezot, Étienne Aumont, and others. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. Nature neuroscience, 25(11):1569–1581, 2022.
    - James W Murrough, Shannan Henry, Jian Hu, Jean-Dominique Gallezot, Beata Planeta-Wilson, John F Neumaier, and Alexander Neumeister. Reduced ventral striatal/ventral pallidal serotonin 1b receptor binding potential in major depressive disorder. Psychopharmacology, 213(2):547–553, 2011.
    - James W Murrough, Christoph Czermak, Shannan Henry, Nabeel Nabulsi, Jean-Dominique Gallezot, Ralitza Gueorguieva, Beata Planeta-Wilson, John H Krystal, John F Neumaier, Yiyun Huang, and others. The effect of early trauma exposure on serotonin type 1b receptor expression revealed by reduced selective radioligand binding. Archives of general psychiatry, 68(9):892–900, 2011.
    - David Matuskey, Zubin Bhagwagar, Beata Planeta, Brian Pittman, Jean-Dominique Gallezot, Jason Chen, Jane Wanyiri, Soheila Najafzadeh, Jim Ropchan, Paul Geha, and others. Reductions in brain 5-ht1b receptor availability in primarily cocaine-dependent humans. Biological psychiatry, 76(10):816–822, 2014.
    - Christopher Pittenger, Thomas G Adams Jr, Jean-Dominique Gallezot, Michael J Crowley, Nabeel Nabulsi, James Ropchan, Hong Gao, Stephen A Kichuk, Ryan Simpson, Eileen Billingslea, and others. Ocd is associated with an altered association between sensorimotor gating and cortical and subcortical 5-ht1b receptor binding. Journal of affective disorders, 196:87–96, 2016.
    - Aybala Saricicek, Jason Chen, Beata Planeta, Barbara Ruf, Kalyani Subramanyam, Kathleen Maloney, David Matuskey, David Labaree, Lorenz Deserno, Alexander Neumeister, and others. Test–retest reliability of the novel 5-ht 1b receptor pet radioligand [11 c] p943. European journal of nuclear medicine and molecular imaging, 42(3):468–477, 2015.
    - Stephen R Baldassarri, Eunkyung Park, Sjoerd J Finnema, Beata Planeta, Nabeel Nabulsi, Soheila Najafzadeh, Jim Ropchan, Yiyun Huang, Jonas Hannestad, Kathleen Maloney, and others. Inverse changes in raphe and cortical 5-ht1b receptor availability after acute tryptophan depletion in healthy human subjects. Synapse, 74(10):e22159, 2020.

----

gallezot2017-gsk189254-MNI152-1mm
=================================

**Annotation identifier**

*{'source': 'gallezot2017', 'desc': 'gsk189254', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (Vt) to H3 (histamine receptor)

**Demographics**: N = 8, Age = 31.69 +- 8.95

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='gallezot2017', desc='gsk189254', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('gallezot2017', 'gsk189254', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/gallezot2017/gsk189254/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-gallezot2017_desc-gsk189254_space-MNI152_res-1mm_feature.nii.gz

**References**
    - Jean-Dominique Gallezot, Nabeel Nabulsi, Alexander Neumeister, Beata Planeta-Wilson, Wendol A Williams, Tarun Singhal, Sunhee Kim, R Paul Maguire, Timothy McCarthy, J James Frost, and others. Kinetic modeling of the serotonin 5-ht1b receptor radioligand [11c] p943 in humans. Journal of Cerebral Blood Flow & Metabolism, 30(1):196–210, 2010.
    - Justine Y Hansen, Golia Shafiei, Ross D Markello, Kelly Smart, Sylvia ML Cox, Martin Nørgaard, Vincent Beliveau, Yanjun Wu, Jean-Dominique Gallezot, Étienne Aumont, and others. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. Nature neuroscience, 25(11):1569–1581, 2022.
    - Sharon Ashworth, Eugenii A Rabiner, Roger N Gunn, Christophe Plisson, Alan A Wilson, Robert A Comley, Robert YK Lai, Antony D Gee, Marc Laruelle, and Vincent J Cunningham. Evaluation of 11c-gsk189254 as a novel radioligand for the h3 receptor in humans using pet. Journal of Nuclear Medicine, 51(7):1021–1029, 2010.

----

hcps1200-megalpha-fsLR-4k
=========================

**Annotation identifier**

*{'source': 'hcps1200', 'desc': 'megalpha', 'space': 'fsLR', 'den': '4k'}*

**Full description**

MEG alpha (8-12 Hz) power distribution from the Human Connectome Project S1200 release

**Demographics**: N = 33, Age = 22-35

**Tags**: functional, MEG

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='hcps1200', desc='megalpha', space='fsLR', den='4k')

    # describe annotation
    describe_annotations(('hcps1200', 'megalpha', 'fsLR', '4k'))

    # file location
    # $NEUROMAPS_DATA/hcps1200/megalpha/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-hcps1200_desc-megalpha_space-fsLR_den-4k_hemi-L_feature.func.gii

**References**
    - David C Van Essen, Stephen M Smith, Deanna M Barch, Timothy EJ Behrens, Essa Yacoub, Kamil Ugurbil, Wu-Minn HCP Consortium, and others. The wu-minn human connectome project: an overview. Neuroimage, 80:62–79, 2013.
    - Golia Shafiei, Sylvain Baillet, and Bratislav Misic. Human electromagnetic and haemodynamic networks systematically converge in unimodal cortex and diverge in transmodal cortex. PLoS biology, 20(8):e3001735, 2022.

----

hcps1200-megbeta-fsLR-4k
========================

**Annotation identifier**

*{'source': 'hcps1200', 'desc': 'megbeta', 'space': 'fsLR', 'den': '4k'}*

**Full description**

MEG beta (15-29 Hz) power distribution from the Human Connectome Project S1200 release

**Demographics**: N = 33, Age = 22-35

**Tags**: functional, MEG

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='hcps1200', desc='megbeta', space='fsLR', den='4k')

    # describe annotation
    describe_annotations(('hcps1200', 'megbeta', 'fsLR', '4k'))

    # file location
    # $NEUROMAPS_DATA/hcps1200/megbeta/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-hcps1200_desc-megbeta_space-fsLR_den-4k_hemi-L_feature.func.gii

**References**
    - David C Van Essen, Stephen M Smith, Deanna M Barch, Timothy EJ Behrens, Essa Yacoub, Kamil Ugurbil, Wu-Minn HCP Consortium, and others. The wu-minn human connectome project: an overview. Neuroimage, 80:62–79, 2013.
    - Golia Shafiei, Sylvain Baillet, and Bratislav Misic. Human electromagnetic and haemodynamic networks systematically converge in unimodal cortex and diverge in transmodal cortex. PLoS biology, 20(8):e3001735, 2022.

----

hcps1200-megdelta-fsLR-4k
=========================

**Annotation identifier**

*{'source': 'hcps1200', 'desc': 'megdelta', 'space': 'fsLR', 'den': '4k'}*

**Full description**

MEG delta (2-4 Hz) power distribution from the Human Connectome Project S1200 release

**Demographics**: N = 33, Age = 22-35

**Tags**: functional, MEG

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='hcps1200', desc='megdelta', space='fsLR', den='4k')

    # describe annotation
    describe_annotations(('hcps1200', 'megdelta', 'fsLR', '4k'))

    # file location
    # $NEUROMAPS_DATA/hcps1200/megdelta/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-hcps1200_desc-megdelta_space-fsLR_den-4k_hemi-L_feature.func.gii

**References**
    - David C Van Essen, Stephen M Smith, Deanna M Barch, Timothy EJ Behrens, Essa Yacoub, Kamil Ugurbil, Wu-Minn HCP Consortium, and others. The wu-minn human connectome project: an overview. Neuroimage, 80:62–79, 2013.
    - Golia Shafiei, Sylvain Baillet, and Bratislav Misic. Human electromagnetic and haemodynamic networks systematically converge in unimodal cortex and diverge in transmodal cortex. PLoS biology, 20(8):e3001735, 2022.

----

hcps1200-meggamma1-fsLR-4k
==========================

**Annotation identifier**

*{'source': 'hcps1200', 'desc': 'meggamma1', 'space': 'fsLR', 'den': '4k'}*

**Full description**

MEG low gamma (30-59 Hz) power distribution from the Human Connectome Project S1200 release

**Demographics**: N = 33, Age = 22-35

**Tags**: functional, MEG

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='hcps1200', desc='meggamma1', space='fsLR', den='4k')

    # describe annotation
    describe_annotations(('hcps1200', 'meggamma1', 'fsLR', '4k'))

    # file location
    # $NEUROMAPS_DATA/hcps1200/meggamma1/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-hcps1200_desc-meggamma1_space-fsLR_den-4k_hemi-L_feature.func.gii

**References**
    - David C Van Essen, Stephen M Smith, Deanna M Barch, Timothy EJ Behrens, Essa Yacoub, Kamil Ugurbil, Wu-Minn HCP Consortium, and others. The wu-minn human connectome project: an overview. Neuroimage, 80:62–79, 2013.
    - Golia Shafiei, Sylvain Baillet, and Bratislav Misic. Human electromagnetic and haemodynamic networks systematically converge in unimodal cortex and diverge in transmodal cortex. PLoS biology, 20(8):e3001735, 2022.

----

hcps1200-meggamma2-fsLR-4k
==========================

**Annotation identifier**

*{'source': 'hcps1200', 'desc': 'meggamma2', 'space': 'fsLR', 'den': '4k'}*

**Full description**

MEG high gamma (60-90 Hz) power distribution from the Human Connectome Project S1200 release

**Demographics**: N = 33, Age = 22-35

**Tags**: functional, MEG

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='hcps1200', desc='meggamma2', space='fsLR', den='4k')

    # describe annotation
    describe_annotations(('hcps1200', 'meggamma2', 'fsLR', '4k'))

    # file location
    # $NEUROMAPS_DATA/hcps1200/meggamma2/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-hcps1200_desc-meggamma2_space-fsLR_den-4k_hemi-L_feature.func.gii

**References**
    - David C Van Essen, Stephen M Smith, Deanna M Barch, Timothy EJ Behrens, Essa Yacoub, Kamil Ugurbil, Wu-Minn HCP Consortium, and others. The wu-minn human connectome project: an overview. Neuroimage, 80:62–79, 2013.
    - Golia Shafiei, Sylvain Baillet, and Bratislav Misic. Human electromagnetic and haemodynamic networks systematically converge in unimodal cortex and diverge in transmodal cortex. PLoS biology, 20(8):e3001735, 2022.

----

hcps1200-megtheta-fsLR-4k
=========================

**Annotation identifier**

*{'source': 'hcps1200', 'desc': 'megtheta', 'space': 'fsLR', 'den': '4k'}*

**Full description**

MEG theta (5-7 Hz) power distribution from the Human Connectome Project S1200 release

**Demographics**: N = 33, Age = 22-35

**Tags**: functional, MEG

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='hcps1200', desc='megtheta', space='fsLR', den='4k')

    # describe annotation
    describe_annotations(('hcps1200', 'megtheta', 'fsLR', '4k'))

    # file location
    # $NEUROMAPS_DATA/hcps1200/megtheta/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-hcps1200_desc-megtheta_space-fsLR_den-4k_hemi-L_feature.func.gii

**References**
    - David C Van Essen, Stephen M Smith, Deanna M Barch, Timothy EJ Behrens, Essa Yacoub, Kamil Ugurbil, Wu-Minn HCP Consortium, and others. The wu-minn human connectome project: an overview. Neuroimage, 80:62–79, 2013.
    - Golia Shafiei, Sylvain Baillet, and Bratislav Misic. Human electromagnetic and haemodynamic networks systematically converge in unimodal cortex and diverge in transmodal cortex. PLoS biology, 20(8):e3001735, 2022.

----

hcps1200-megtimescale-fsLR-4k
=============================

**Annotation identifier**

*{'source': 'hcps1200', 'desc': 'megtimescale', 'space': 'fsLR', 'den': '4k'}*

**Full description**

MEG intrinsic timescale from the Human Connectome Project S1200 release

**Demographics**: N = 33, Age = 22-35

**Tags**: functional, MEG

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='hcps1200', desc='megtimescale', space='fsLR', den='4k')

    # describe annotation
    describe_annotations(('hcps1200', 'megtimescale', 'fsLR', '4k'))

    # file location
    # $NEUROMAPS_DATA/hcps1200/megtimescale/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-hcps1200_desc-megtimescale_space-fsLR_den-4k_hemi-L_feature.func.gii

**References**
    - David C Van Essen, Stephen M Smith, Deanna M Barch, Timothy EJ Behrens, Essa Yacoub, Kamil Ugurbil, Wu-Minn HCP Consortium, and others. The wu-minn human connectome project: an overview. Neuroimage, 80:62–79, 2013.
    - Golia Shafiei, Sylvain Baillet, and Bratislav Misic. Human electromagnetic and haemodynamic networks systematically converge in unimodal cortex and diverge in transmodal cortex. PLoS biology, 20(8):e3001735, 2022.

----

hcps1200-myelinmap-fsLR-32k
===========================

**Annotation identifier**

*{'source': 'hcps1200', 'desc': 'myelinmap', 'space': 'fsLR', 'den': '32k'}*

**Full description**

MRI T1w/T2w ratio from the Human Connectome Project S1200 release

**Demographics**: N = None, Age = 22-35

**Tags**: structural, MRI

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='hcps1200', desc='myelinmap', space='fsLR', den='32k')

    # describe annotation
    describe_annotations(('hcps1200', 'myelinmap', 'fsLR', '32k'))

    # file location
    # $NEUROMAPS_DATA/hcps1200/myelinmap/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-hcps1200_desc-myelinmap_space-fsLR_den-32k_hemi-L_feature.func.gii

**References**
    - Matthew F Glasser, Timothy S Coalson, Emma C Robinson, Carl D Hacker, John Harwell, Essa Yacoub, Kamil Ugurbil, Jesper Andersson, Christian F Beckmann, Mark Jenkinson, and others. A multi-modal parcellation of human cerebral cortex. Nature, 536(7615):171–178, 2016.

----

hcps1200-thickness-fsLR-32k
===========================

**Annotation identifier**

*{'source': 'hcps1200', 'desc': 'thickness', 'space': 'fsLR', 'den': '32k'}*

**Full description**

MRI cortical thickness from the Human Connectome Project S1200 release

**Demographics**: N = None, Age = 22-35

**Tags**: structural, MRI

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='hcps1200', desc='thickness', space='fsLR', den='32k')

    # describe annotation
    describe_annotations(('hcps1200', 'thickness', 'fsLR', '32k'))

    # file location
    # $NEUROMAPS_DATA/hcps1200/thickness/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-hcps1200_desc-thickness_space-fsLR_den-32k_hemi-L_feature.func.gii

**References**
    - Matthew F Glasser, Timothy S Coalson, Emma C Robinson, Carl D Hacker, John Harwell, Essa Yacoub, Kamil Ugurbil, Jesper Andersson, Christian F Beckmann, Mark Jenkinson, and others. A multi-modal parcellation of human cerebral cortex. Nature, 536(7615):171–178, 2016.

----

hesse2017-methylreboxetine-MNI152-3mm
=====================================

**Annotation identifier**

*{'source': 'hesse2017', 'desc': 'methylreboxetine', 'space': 'MNI152', 'res': '3mm'}*

**Full description**

PET tracer binding (BPnd) to NET (norepinephrine transporter)

**Demographics**: N = 10, Age = 33.3 (mean)

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='hesse2017', desc='methylreboxetine', space='MNI152', res='3mm')

    # describe annotation
    describe_annotations(('hesse2017', 'methylreboxetine', 'MNI152', '3mm'))

    # file location
    # $NEUROMAPS_DATA/hesse2017/methylreboxetine/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-hesse2017_desc-methylreboxetine_space-MNI152_res-3mm_feature.nii.gz

**References**
    - Swen Hesse, Georg-Alexander Becker, Michael Rullmann, Anke Bresch, Julia Luthardt, Mohammed K Hankir, Franziska Zientek, Georg Reißig, Marianne Patt, Katrin Arelin, and others. Central noradrenaline transporter availability in highly obese, non-depressed individuals. European journal of nuclear medicine and molecular imaging, 44(6):1056–1064, 2017.

----

hill2010-devexp-fsLR-164k
=========================

**Annotation identifier**

*{'source': 'hill2010', 'desc': 'devexp', 'space': 'fsLR', 'den': '164k'}*

**Full description**

Developmental cortical expansion

**Demographics**: N = None, Age = None

**Tags**: structural, MRI

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='hill2010', desc='devexp', space='fsLR', den='164k')

    # describe annotation
    describe_annotations(('hill2010', 'devexp', 'fsLR', '164k'))

    # file location
    # $NEUROMAPS_DATA/hill2010/devexp/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-hill2010_desc-devexp_space-fsLR_den-164k_hemi-R_feature.func.gii

**References**
    - Jason Hill, Terrie Inder, Jeffrey Neil, Donna Dierker, John Harwell, and David Van Essen. Similar patterns of cortical expansion during human development and evolution. Proceedings of the National Academy of Sciences, 107(29):13135–13140, 2010.

----

hill2010-evoexp-fsLR-164k
=========================

**Annotation identifier**

*{'source': 'hill2010', 'desc': 'evoexp', 'space': 'fsLR', 'den': '164k'}*

**Full description**

Evolutionary cortical expansion

**Demographics**: N = None, Age = None

**Tags**: structural, MRI

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='hill2010', desc='evoexp', space='fsLR', den='164k')

    # describe annotation
    describe_annotations(('hill2010', 'evoexp', 'fsLR', '164k'))

    # file location
    # $NEUROMAPS_DATA/hill2010/evoexp/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-hill2010_desc-evoexp_space-fsLR_den-164k_hemi-R_feature.func.gii

**References**
    - Jason Hill, Terrie Inder, Jeffrey Neil, Donna Dierker, John Harwell, and David Van Essen. Similar patterns of cortical expansion during human development and evolution. Proceedings of the National Academy of Sciences, 107(29):13135–13140, 2010.

----

hillmer2016-flubatine-MNI152-1mm
================================

**Annotation identifier**

*{'source': 'hillmer2016', 'desc': 'flubatine', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (Vt) to a4b2 (acetylcholine receptor)

**Demographics**: N = 30, Age = 33.50 +/- 10.71

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='hillmer2016', desc='flubatine', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('hillmer2016', 'flubatine', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/hillmer2016/flubatine/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-hillmer2016_desc-flubatine_space-MNI152_res-1mm_feature.nii.gz

**References**
    - Ansel T Hillmer, I Esterlis, Jean-Dominique Gallezot, F Bois, Ming-Qiang Zheng, Nabeel Nabulsi, Shu-Fei Lin, RL Papke, Yiyun Huang, Osama Sabri, and others. Imaging of cerebral α4β2* nicotinic acetylcholine receptors with (-)-[18f] flubatine pet: implementation of bolus plus constant infusion and sensitivity to acetylcholine in human brain. Neuroimage, 141:71–80, 2016.
    - Justine Y Hansen, Golia Shafiei, Ross D Markello, Kelly Smart, Sylvia ML Cox, Martin Nørgaard, Vincent Beliveau, Yanjun Wu, Jean-Dominique Gallezot, Étienne Aumont, and others. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. Nature neuroscience, 25(11):1569–1581, 2022.
    - Stephen R Baldassarri, Ansel T Hillmer, Jon Mikael Anderson, Peter Jatlow, Nabeel Nabulsi, David Labaree, Kelly P Cosgrove, Stephanie S O’Malley, Thomas Eissenberg, Suchitra Krishnan-Sarin, and others. Use of electronic cigarettes leads to significant beta2-nicotinic acetylcholine receptor occupancy: evidence from a pet imaging study. Nicotine and Tobacco Research, 20(4):425–433, 2018.

----

jaworska2020-fallypride-MNI152-1mm
==================================

**Annotation identifier**

*{'source': 'jaworska2020', 'desc': 'fallypride', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (BPnd) to D2 (dopamine receptor)

**Demographics**: N = 49, Age = 18.41 +/- 0.57

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='jaworska2020', desc='fallypride', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('jaworska2020', 'fallypride', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/jaworska2020/fallypride/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-jaworska2020_desc-fallypride_space-MNI152_res-1mm_feature.nii.gz

**References**
    - Natalia Jaworska, Sylvia ML Cox, Maria Tippler, Natalie Castellanos-Ryan, Chawki Benkelfat, Sophie Parent, Alain Dagher, Frank Vitaro, Michel Boivin, Robert O Pihl, and others. Extra-striatal d 2/3 receptor availability in youth at risk for addiction. Neuropsychopharmacology, 45(9):1498–1505, 2020.
    - Justine Y Hansen, Golia Shafiei, Ross D Markello, Kelly Smart, Sylvia ML Cox, Martin Nørgaard, Vincent Beliveau, Yanjun Wu, Jean-Dominique Gallezot, Étienne Aumont, and others. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. Nature neuroscience, 25(11):1569–1581, 2022.

----

kaller2017-sch23390-MNI152-3mm
==============================

**Annotation identifier**

*{'source': 'kaller2017', 'desc': 'sch23390', 'space': 'MNI152', 'res': '3mm'}*

**Full description**

PET tracer binding (BPnd) to D1 (dopamine receptor)

**Demographics**: N = 13, Age = 33 +/- 13

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='kaller2017', desc='sch23390', space='MNI152', res='3mm')

    # describe annotation
    describe_annotations(('kaller2017', 'sch23390', 'MNI152', '3mm'))

    # file location
    # $NEUROMAPS_DATA/kaller2017/sch23390/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-kaller2017_desc-sch23390_space-MNI152_res-3mm_feature.nii.gz

**References**
    - Simon Kaller, Michael Rullmann, Marianne Patt, Georg-Alexander Becker, Julia Luthardt, Johanna Girbardt, Philipp M Meyer, Peter Werner, Henryk Barthel, Anke Bresch, and others. Test–retest measurements of dopamine d 1-type receptors using simultaneous pet/mri imaging. European journal of nuclear medicine and molecular imaging, 44(6):1025–1032, 2017.

----

kantonen2020-carfentanil-MNI152-3mm
===================================

**Annotation identifier**

*{'source': 'kantonen2020', 'desc': 'carfentanil', 'space': 'MNI152', 'res': '3mm'}*

**Full description**

PET tracer binding (BPnd) to MOR (mu-opioid receptor)

**Demographics**: N = 204, Age = 32.3 +/- 10.8

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='kantonen2020', desc='carfentanil', space='MNI152', res='3mm')

    # describe annotation
    describe_annotations(('kantonen2020', 'carfentanil', 'MNI152', '3mm'))

    # file location
    # $NEUROMAPS_DATA/kantonen2020/carfentanil/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-kantonen2020_desc-carfentanil_space-MNI152_res-3mm_feature.nii.gz

**References**
    - Tatu Kantonen, Tomi Karjalainen, Janne Isojärvi, Pirjo Nuutila, Jouni Tuisku, Juha Rinne, Jarmo Hietala, Valtteri Kaasinen, Kari Kalliokoski, Harry Scheinin, and others. Interindividual variability and lateralization of µ-opioid receptors in the human brain. NeuroImage, 217:116922, 2020.

----

laurikainen2018-fmpepd2-MNI152-1mm
==================================

**Annotation identifier**

*{'source': 'laurikainen2018', 'desc': 'fmpepd2', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (Vt) to CB1 (cannabinoid receptor)

**Demographics**: N = 22, Age = 27.5 +/- 8.05

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='laurikainen2018', desc='fmpepd2', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('laurikainen2018', 'fmpepd2', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/laurikainen2018/fmpepd2/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-laurikainen2018_desc-fmpepd2_space-MNI152_res-1mm_feature.nii.gz

**References**
    - Heikki Laurikainen, Lauri Tuominen, Maria Tikka, Harri Merisaari, Reetta-Liina Armio, Elina Sormunen, Faith Borgan, Mattia Veronese, Oliver Howes, Merja Haaparanta-Solin, and others. Sex difference in brain cb1 receptor availability in man. Neuroimage, 184:834–842, 2019.

----

margulies2016-fcgradient01-fsLR-32k
===================================

**Annotation identifier**

*{'source': 'margulies2016', 'desc': 'fcgradient01', 'space': 'fsLR', 'den': '32k'}*

**Full description**

Diffusion map embedding gradient 1 of group-averaged functional connectivity

**Demographics**: N = 820, Age = None

**Tags**: functional, MRI, fMRI

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='margulies2016', desc='fcgradient01', space='fsLR', den='32k')

    # describe annotation
    describe_annotations(('margulies2016', 'fcgradient01', 'fsLR', '32k'))

    # file location
    # $NEUROMAPS_DATA/margulies2016/fcgradient01/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-margulies2016_desc-fcgradient01_space-fsLR_den-32k_hemi-L_feature.func.gii

**References**
    - Daniel S Margulies, Satrajit S Ghosh, Alexandros Goulas, Marcel Falkiewicz, Julia M Huntenburg, Georg Langs, Gleb Bezgin, Simon B Eickhoff, F Xavier Castellanos, Michael Petrides, and others. Situating the default-mode network along a principal gradient of macroscale cortical organization. Proc Natl Acad Sci USA, 113(44):12574–12579, 2016.

----

margulies2016-fcgradient02-fsLR-32k
===================================

**Annotation identifier**

*{'source': 'margulies2016', 'desc': 'fcgradient02', 'space': 'fsLR', 'den': '32k'}*

**Full description**

Diffusion map embedding gradient 2 of group-averaged functional connectivity

**Demographics**: N = 820, Age = None

**Tags**: functional, MRI, fMRI

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='margulies2016', desc='fcgradient02', space='fsLR', den='32k')

    # describe annotation
    describe_annotations(('margulies2016', 'fcgradient02', 'fsLR', '32k'))

    # file location
    # $NEUROMAPS_DATA/margulies2016/fcgradient02/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-margulies2016_desc-fcgradient02_space-fsLR_den-32k_hemi-L_feature.func.gii

**References**
    - Daniel S Margulies, Satrajit S Ghosh, Alexandros Goulas, Marcel Falkiewicz, Julia M Huntenburg, Georg Langs, Gleb Bezgin, Simon B Eickhoff, F Xavier Castellanos, Michael Petrides, and others. Situating the default-mode network along a principal gradient of macroscale cortical organization. Proc Natl Acad Sci USA, 113(44):12574–12579, 2016.

----

margulies2016-fcgradient03-fsLR-32k
===================================

**Annotation identifier**

*{'source': 'margulies2016', 'desc': 'fcgradient03', 'space': 'fsLR', 'den': '32k'}*

**Full description**

Diffusion map embedding gradient 3 of group-averaged functional connectivity

**Demographics**: N = 820, Age = None

**Tags**: functional, MRI, fMRI

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='margulies2016', desc='fcgradient03', space='fsLR', den='32k')

    # describe annotation
    describe_annotations(('margulies2016', 'fcgradient03', 'fsLR', '32k'))

    # file location
    # $NEUROMAPS_DATA/margulies2016/fcgradient03/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-margulies2016_desc-fcgradient03_space-fsLR_den-32k_hemi-L_feature.func.gii

**References**
    - Daniel S Margulies, Satrajit S Ghosh, Alexandros Goulas, Marcel Falkiewicz, Julia M Huntenburg, Georg Langs, Gleb Bezgin, Simon B Eickhoff, F Xavier Castellanos, Michael Petrides, and others. Situating the default-mode network along a principal gradient of macroscale cortical organization. Proc Natl Acad Sci USA, 113(44):12574–12579, 2016.

----

margulies2016-fcgradient04-fsLR-32k
===================================

**Annotation identifier**

*{'source': 'margulies2016', 'desc': 'fcgradient04', 'space': 'fsLR', 'den': '32k'}*

**Full description**

Diffusion map embedding gradient 4 of group-averaged functional connectivity

**Demographics**: N = 820, Age = None

**Tags**: functional, MRI, fMRI

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='margulies2016', desc='fcgradient04', space='fsLR', den='32k')

    # describe annotation
    describe_annotations(('margulies2016', 'fcgradient04', 'fsLR', '32k'))

    # file location
    # $NEUROMAPS_DATA/margulies2016/fcgradient04/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-margulies2016_desc-fcgradient04_space-fsLR_den-32k_hemi-L_feature.func.gii

**References**
    - Daniel S Margulies, Satrajit S Ghosh, Alexandros Goulas, Marcel Falkiewicz, Julia M Huntenburg, Georg Langs, Gleb Bezgin, Simon B Eickhoff, F Xavier Castellanos, Michael Petrides, and others. Situating the default-mode network along a principal gradient of macroscale cortical organization. Proc Natl Acad Sci USA, 113(44):12574–12579, 2016.

----

margulies2016-fcgradient05-fsLR-32k
===================================

**Annotation identifier**

*{'source': 'margulies2016', 'desc': 'fcgradient05', 'space': 'fsLR', 'den': '32k'}*

**Full description**

Diffusion map embedding gradient 5 of group-averaged functional connectivity

**Demographics**: N = 820, Age = None

**Tags**: functional, MRI, fMRI

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='margulies2016', desc='fcgradient05', space='fsLR', den='32k')

    # describe annotation
    describe_annotations(('margulies2016', 'fcgradient05', 'fsLR', '32k'))

    # file location
    # $NEUROMAPS_DATA/margulies2016/fcgradient05/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-margulies2016_desc-fcgradient05_space-fsLR_den-32k_hemi-L_feature.func.gii

**References**
    - Daniel S Margulies, Satrajit S Ghosh, Alexandros Goulas, Marcel Falkiewicz, Julia M Huntenburg, Georg Langs, Gleb Bezgin, Simon B Eickhoff, F Xavier Castellanos, Michael Petrides, and others. Situating the default-mode network along a principal gradient of macroscale cortical organization. Proc Natl Acad Sci USA, 113(44):12574–12579, 2016.

----

margulies2016-fcgradient06-fsLR-32k
===================================

**Annotation identifier**

*{'source': 'margulies2016', 'desc': 'fcgradient06', 'space': 'fsLR', 'den': '32k'}*

**Full description**

Diffusion map embedding gradient 6 of group-averaged functional connectivity

**Demographics**: N = 820, Age = None

**Tags**: functional, MRI, fMRI

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='margulies2016', desc='fcgradient06', space='fsLR', den='32k')

    # describe annotation
    describe_annotations(('margulies2016', 'fcgradient06', 'fsLR', '32k'))

    # file location
    # $NEUROMAPS_DATA/margulies2016/fcgradient06/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-margulies2016_desc-fcgradient06_space-fsLR_den-32k_hemi-L_feature.func.gii

**References**
    - Daniel S Margulies, Satrajit S Ghosh, Alexandros Goulas, Marcel Falkiewicz, Julia M Huntenburg, Georg Langs, Gleb Bezgin, Simon B Eickhoff, F Xavier Castellanos, Michael Petrides, and others. Situating the default-mode network along a principal gradient of macroscale cortical organization. Proc Natl Acad Sci USA, 113(44):12574–12579, 2016.

----

margulies2016-fcgradient07-fsLR-32k
===================================

**Annotation identifier**

*{'source': 'margulies2016', 'desc': 'fcgradient07', 'space': 'fsLR', 'den': '32k'}*

**Full description**

Diffusion map embedding gradient 7 of group-averaged functional connectivity

**Demographics**: N = 820, Age = None

**Tags**: functional, MRI, fMRI

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='margulies2016', desc='fcgradient07', space='fsLR', den='32k')

    # describe annotation
    describe_annotations(('margulies2016', 'fcgradient07', 'fsLR', '32k'))

    # file location
    # $NEUROMAPS_DATA/margulies2016/fcgradient07/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-margulies2016_desc-fcgradient07_space-fsLR_den-32k_hemi-L_feature.func.gii

**References**
    - Daniel S Margulies, Satrajit S Ghosh, Alexandros Goulas, Marcel Falkiewicz, Julia M Huntenburg, Georg Langs, Gleb Bezgin, Simon B Eickhoff, F Xavier Castellanos, Michael Petrides, and others. Situating the default-mode network along a principal gradient of macroscale cortical organization. Proc Natl Acad Sci USA, 113(44):12574–12579, 2016.

----

margulies2016-fcgradient08-fsLR-32k
===================================

**Annotation identifier**

*{'source': 'margulies2016', 'desc': 'fcgradient08', 'space': 'fsLR', 'den': '32k'}*

**Full description**

Diffusion map embedding gradient 8 of group-averaged functional connectivity

**Demographics**: N = 820, Age = None

**Tags**: functional, MRI, fMRI

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='margulies2016', desc='fcgradient08', space='fsLR', den='32k')

    # describe annotation
    describe_annotations(('margulies2016', 'fcgradient08', 'fsLR', '32k'))

    # file location
    # $NEUROMAPS_DATA/margulies2016/fcgradient08/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-margulies2016_desc-fcgradient08_space-fsLR_den-32k_hemi-L_feature.func.gii

**References**
    - Daniel S Margulies, Satrajit S Ghosh, Alexandros Goulas, Marcel Falkiewicz, Julia M Huntenburg, Georg Langs, Gleb Bezgin, Simon B Eickhoff, F Xavier Castellanos, Michael Petrides, and others. Situating the default-mode network along a principal gradient of macroscale cortical organization. Proc Natl Acad Sci USA, 113(44):12574–12579, 2016.

----

margulies2016-fcgradient09-fsLR-32k
===================================

**Annotation identifier**

*{'source': 'margulies2016', 'desc': 'fcgradient09', 'space': 'fsLR', 'den': '32k'}*

**Full description**

Diffusion map embedding gradient 9 of group-averaged functional connectivity

**Demographics**: N = 820, Age = None

**Tags**: functional, MRI, fMRI

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='margulies2016', desc='fcgradient09', space='fsLR', den='32k')

    # describe annotation
    describe_annotations(('margulies2016', 'fcgradient09', 'fsLR', '32k'))

    # file location
    # $NEUROMAPS_DATA/margulies2016/fcgradient09/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-margulies2016_desc-fcgradient09_space-fsLR_den-32k_hemi-L_feature.func.gii

**References**
    - Daniel S Margulies, Satrajit S Ghosh, Alexandros Goulas, Marcel Falkiewicz, Julia M Huntenburg, Georg Langs, Gleb Bezgin, Simon B Eickhoff, F Xavier Castellanos, Michael Petrides, and others. Situating the default-mode network along a principal gradient of macroscale cortical organization. Proc Natl Acad Sci USA, 113(44):12574–12579, 2016.

----

margulies2016-fcgradient10-fsLR-32k
===================================

**Annotation identifier**

*{'source': 'margulies2016', 'desc': 'fcgradient10', 'space': 'fsLR', 'den': '32k'}*

**Full description**

Diffusion map embedding gradient 10 of group-averaged functional connectivity

**Demographics**: N = 820, Age = None

**Tags**: functional, MRI, fMRI

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='margulies2016', desc='fcgradient10', space='fsLR', den='32k')

    # describe annotation
    describe_annotations(('margulies2016', 'fcgradient10', 'fsLR', '32k'))

    # file location
    # $NEUROMAPS_DATA/margulies2016/fcgradient10/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-margulies2016_desc-fcgradient10_space-fsLR_den-32k_hemi-L_feature.func.gii

**References**
    - Daniel S Margulies, Satrajit S Ghosh, Alexandros Goulas, Marcel Falkiewicz, Julia M Huntenburg, Georg Langs, Gleb Bezgin, Simon B Eickhoff, F Xavier Castellanos, Michael Petrides, and others. Situating the default-mode network along a principal gradient of macroscale cortical organization. Proc Natl Acad Sci USA, 113(44):12574–12579, 2016.

----

mueller2013-intersubjvar-fsLR-164k
==================================

**Annotation identifier**

*{'source': 'mueller2013', 'desc': 'intersubjvar', 'space': 'fsLR', 'den': '164k'}*

**Full description**

Intersubject variability of resting-state functional connectivity.

**Demographics**: N = 25, Age = 51.8 +/- 6.99

**Tags**: functional, MRI, fMRI

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='mueller2013', desc='intersubjvar', space='fsLR', den='164k')

    # describe annotation
    describe_annotations(('mueller2013', 'intersubjvar', 'fsLR', '164k'))

    # file location
    # $NEUROMAPS_DATA/mueller2013/intersubjvar/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-mueller2013_desc-intersubjvar_space-fsLR_den-164k_hemi-L_feature.func.gii

**References**
    - Sophia Mueller, Danhong Wang, Michael D Fox, BT Thomas Yeo, Jorge Sepulcre, Mert R Sabuncu, Rebecca Shafee, Jie Lu, and Hesheng Liu. Individual variability in functional connectivity architecture of the human brain. Neuron, 77(3):586–595, 2013.

----

naganawa2020-lsn3172176-MNI152-1mm
==================================

**Annotation identifier**

*{'source': 'naganawa2020', 'desc': 'lsn3172176', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (BPnd) to M1 (acetylcholine receptor)

**Demographics**: N = 24, Age = 40.45 +/- 11.71

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='naganawa2020', desc='lsn3172176', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('naganawa2020', 'lsn3172176', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/naganawa2020/lsn3172176/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-naganawa2020_desc-lsn3172176_space-MNI152_res-1mm_feature.nii.gz

**References**
    - Mika Naganawa, Nabeel Nabulsi, Shannan Henry, David Matuskey, Shu-Fei Lin, Lawrence Slieker, Adam J Schwarz, Nancy Kant, Cynthia Jesudason, Kevin Ruley, and others. First-in-human assessment of 11c-lsn3172176, an m1 muscarinic acetylcholine receptor pet radiotracer. Journal of Nuclear Medicine, 62(4):553–560, 2021.
    - Justine Y Hansen, Golia Shafiei, Ross D Markello, Kelly Smart, Sylvia ML Cox, Martin Nørgaard, Vincent Beliveau, Yanjun Wu, Jean-Dominique Gallezot, Étienne Aumont, and others. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. Nature neuroscience, 25(11):1569–1581, 2022.

----

neurosynth-cogpc1-MNI152-2mm
============================

**Annotation identifier**

*{'source': 'neurosynth', 'desc': 'cogpc1', 'space': 'MNI152', 'res': '2mm'}*

**Full description**

PC1 of Neurosynth terms in the Cognitive Atlas (123 terms total)

**Demographics**: N = None, Age = None

**Tags**: functional, structural, meta-analysis, MRI, fMRI

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='neurosynth', desc='cogpc1', space='MNI152', res='2mm')

    # describe annotation
    describe_annotations(('neurosynth', 'cogpc1', 'MNI152', '2mm'))

    # file location
    # $NEUROMAPS_DATA/neurosynth/cogpc1/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-neurosynth_desc-cogpc1_space-MNI152_res-2mm_feature.nii.gz

**References**
    - Tal Yarkoni, Russell A Poldrack, Thomas E Nichols, David C Van Essen, and Tor D Wager. Large-scale automated synthesis of human functional neuroimaging data. Nature Methods, 8(8):665, 2011.
    - Russell A Poldrack, Aniket Kittur, Donald Kalar, Eric Miller, Christian Seppa, Yolanda Gil, D Stott Parker, Fred W Sabb, and Robert M Bilder. The cognitive atlas: toward a knowledge foundation for cognitive neuroscience. Frontiers Neuroinform, 5:17, 2011.

----

norgaard2021-flumazenil-MNI152-1mm
==================================

**Annotation identifier**

*{'source': 'norgaard2021', 'desc': 'flumazenil', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET and autoradiography informed GABAa benzodiazepine binding-site density (Bmax; gaba receptor)

**Demographics**: N = 16, Age = 26.6 +/- 8

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='norgaard2021', desc='flumazenil', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('norgaard2021', 'flumazenil', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/norgaard2021/flumazenil/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-norgaard2021_desc-flumazenil_space-MNI152_res-1mm_feature.nii.gz

**Warning**

This annotation is best used in the provided fsaverage space. MNI152 maps should only be used for subcortical data.

**References**
    - Martin Nørgaard, Vincent Beliveau, Melanie Ganz, Claus Svarer, Lars H Pinborg, Sune H Keller, Peter S Jensen, Douglas N Greve, and Gitte M Knudsen. A high-resolution in vivo atlas of the human brain's benzodiazepine binding site of gabaa receptors. NeuroImage, 232:117878, 2021.

----

norgaard2021-flumazenil-fsaverage-164k
======================================

**Annotation identifier**

*{'source': 'norgaard2021', 'desc': 'flumazenil', 'space': 'fsaverage', 'den': '164k'}*

**Full description**

PET and autoradiography informed GABAa benzodiazepine binding-site density (Bmax; gaba receptor)

**Demographics**: N = 16, Age = 26.6 +/- 8

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='norgaard2021', desc='flumazenil', space='fsaverage', den='164k')

    # describe annotation
    describe_annotations(('norgaard2021', 'flumazenil', 'fsaverage', '164k'))

    # file location
    # $NEUROMAPS_DATA/norgaard2021/flumazenil/fsaverage/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-norgaard2021_desc-flumazenil_space-fsaverage_den-164k_hemi-L_feature.func.gii

**References**
    - Martin Nørgaard, Vincent Beliveau, Melanie Ganz, Claus Svarer, Lars H Pinborg, Sune H Keller, Peter S Jensen, Douglas N Greve, and Gitte M Knudsen. A high-resolution in vivo atlas of the human brain's benzodiazepine binding site of gabaa receptors. NeuroImage, 232:117878, 2021.

----

normandin2015-omar-MNI152-1mm
=============================

**Annotation identifier**

*{'source': 'normandin2015', 'desc': 'omar', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (Vt) to CB1 (cannabinoid receptor)

**Demographics**: N = 77, Age = 30.01 +/- 8.87

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='normandin2015', desc='omar', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('normandin2015', 'omar', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/normandin2015/omar/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-normandin2015_desc-omar_space-MNI152_res-1mm_feature.nii.gz

**References**
    - Marc D Normandin, Ming-Qiang Zheng, Kuo-Shyan Lin, N Scott Mason, Shu-Fei Lin, Jim Ropchan, David Labaree, Shannan Henry, Wendol A Williams, Richard E Carson, and others. Imaging the cannabinoid cb1 receptor in humans with [11c] omar: assessment of kinetic analysis methods, test–retest reproducibility, and gender differences. Journal of Cerebral Blood Flow & Metabolism, 35(8):1313–1322, 2015.
    - Deepak Cyril D’Souza, Jose A Cortes-Briones, Mohini Ranganathan, Halle Thurnauer, Gina Creatura, Toral Surti, Beata Planeta, Alexander Neumeister, Brian Pittman, Marc D Normandin, and others. Rapid changes in cannabinoid 1 receptor availability in cannabis-dependent male subjects after abstinence from cannabis. Biological psychiatry: cognitive neuroscience and neuroimaging, 1(1):60–67, 2016.
    - Mohini Ranganathan, Jose Cortes-Briones, Rajiv Radhakrishnan, Halle Thurnauer, Beata Planeta, Patrick Skosnik, Hong Gao, David Labaree, Alexander Neumeister, Brian Pittman, and others. Reduced brain cannabinoid receptor availability in schizophrenia. Biological psychiatry, 79(12):997–1005, 2016.
    - Alexander Neumeister, Marc D Normandin, James W Murrough, Shannan Henry, Christopher R Bailey, David A Luckenbaugh, Keri Tuit, Ming-Qiang Zheng, Isaac R Galatzer-Levy, Rajita Sinha, and others. Positron emission tomography shows elevated cannabinoid cb 1 receptor binding in men with alcohol dependence. Alcoholism: Clinical and Experimental Research, 36(12):2104–2109, 2012.

----

radnakrishnan2018-gsk215083-MNI152-1mm
======================================

**Annotation identifier**

*{'source': 'radnakrishnan2018', 'desc': 'gsk215083', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (BPnd) to 5-HT6 (serotonin receptor)

**Demographics**: N = 30, Age = 36.6 +/- 9.04

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='radnakrishnan2018', desc='gsk215083', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('radnakrishnan2018', 'gsk215083', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/radnakrishnan2018/gsk215083/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-radnakrishnan2018_desc-gsk215083_space-MNI152_res-1mm_feature.nii.gz

**References**
    - Rajiv Radhakrishnan, Nabeel Nabulsi, Edward Gaiser, Jean-Dominique Gallezot, Shannan Henry, Beata Planeta, Shu-fei Lin, Jim Ropchan, Wendol Williams, Evan Morris, and others. Age-related change in 5-ht6 receptor availability in healthy male volunteers measured with 11c-gsk215083 pet. Journal of Nuclear Medicine, 59(9):1445–1450, 2018.
    - Rajiv Radhakrishnan, David Matuskey, Nabeel Nabulsi, Edward Gaiser, Jean-Dominique Gallezot, Shannan Henry, Beata Planeta, Shu-fei Lin, Jim Ropchan, Yiyun Huang, and others. In vivo 5-ht6 and 5-ht2a receptor availability in antipsychotic treated schizophrenia patients vs. unmedicated healthy humans measured with [11c] gsk215083 pet. Psychiatry Research: Neuroimaging, 295:111007, 2020.

----

raichle-cbf-fsLR-164k
=====================

**Annotation identifier**

*{'source': 'raichle', 'desc': 'cbf', 'space': 'fsLR', 'den': '164k'}*

**Full description**

Cerebral blood flow

**Demographics**: N = 33, Age = 25.4 +/- 2.6

**Tags**: functional, PET, metabolism

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='raichle', desc='cbf', space='fsLR', den='164k')

    # describe annotation
    describe_annotations(('raichle', 'cbf', 'fsLR', '164k'))

    # file location
    # $NEUROMAPS_DATA/raichle/cbf/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-raichle_desc-cbf_space-fsLR_den-164k_hemi-L_feature.func.gii

**References**
    - S Neil Vaishnavi, Andrei G Vlassenko, Melissa M Rundle, Abraham Z Snyder, Mark A Mintun, and Marcus E Raichle. Regional aerobic glycolysis in the human brain. Proceedings of the National Academy of Sciences, 107(41):17757–17762, 2010.

----

raichle-cbv-fsLR-164k
=====================

**Annotation identifier**

*{'source': 'raichle', 'desc': 'cbv', 'space': 'fsLR', 'den': '164k'}*

**Full description**

Cerebral blood volume

**Demographics**: N = 33, Age = 25.4 +/- 2.6

**Tags**: functional, PET, metabolism

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='raichle', desc='cbv', space='fsLR', den='164k')

    # describe annotation
    describe_annotations(('raichle', 'cbv', 'fsLR', '164k'))

    # file location
    # $NEUROMAPS_DATA/raichle/cbv/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-raichle_desc-cbv_space-fsLR_den-164k_hemi-L_feature.func.gii

**References**
    - S Neil Vaishnavi, Andrei G Vlassenko, Melissa M Rundle, Abraham Z Snyder, Mark A Mintun, and Marcus E Raichle. Regional aerobic glycolysis in the human brain. Proceedings of the National Academy of Sciences, 107(41):17757–17762, 2010.

----

raichle-cmr02-fsLR-164k
=======================

**Annotation identifier**

*{'source': 'raichle', 'desc': 'cmr02', 'space': 'fsLR', 'den': '164k'}*

**Full description**

Oxygen metabolism

**Demographics**: N = 33, Age = 25.4 +/- 2.6

**Tags**: functional, PET, metabolism

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='raichle', desc='cmr02', space='fsLR', den='164k')

    # describe annotation
    describe_annotations(('raichle', 'cmr02', 'fsLR', '164k'))

    # file location
    # $NEUROMAPS_DATA/raichle/cmr02/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-raichle_desc-cmr02_space-fsLR_den-164k_hemi-L_feature.func.gii

**References**
    - S Neil Vaishnavi, Andrei G Vlassenko, Melissa M Rundle, Abraham Z Snyder, Mark A Mintun, and Marcus E Raichle. Regional aerobic glycolysis in the human brain. Proceedings of the National Academy of Sciences, 107(41):17757–17762, 2010.

----

raichle-cmrglc-fsLR-164k
========================

**Annotation identifier**

*{'source': 'raichle', 'desc': 'cmrglc', 'space': 'fsLR', 'den': '164k'}*

**Full description**

Glucose metabolism

**Demographics**: N = 33, Age = 25.4 +/- 2.6

**Tags**: functional, PET, metabolism

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='raichle', desc='cmrglc', space='fsLR', den='164k')

    # describe annotation
    describe_annotations(('raichle', 'cmrglc', 'fsLR', '164k'))

    # file location
    # $NEUROMAPS_DATA/raichle/cmrglc/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-raichle_desc-cmrglc_space-fsLR_den-164k_hemi-L_feature.func.gii

**References**
    - S Neil Vaishnavi, Andrei G Vlassenko, Melissa M Rundle, Abraham Z Snyder, Mark A Mintun, and Marcus E Raichle. Regional aerobic glycolysis in the human brain. Proceedings of the National Academy of Sciences, 107(41):17757–17762, 2010.

----

reardon2018-scalinghcp-civet-41k
================================

**Annotation identifier**

*{'source': 'reardon2018', 'desc': 'scalinghcp', 'space': 'civet', 'den': '41k'}*

**Full description**

Cortical areal scaling during development from the HCP dataset (S1200 release)

**Demographics**: N = 1113, Age = None

**Tags**: structural, MRI

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='reardon2018', desc='scalinghcp', space='civet', den='41k')

    # describe annotation
    describe_annotations(('reardon2018', 'scalinghcp', 'civet', '41k'))

    # file location
    # $NEUROMAPS_DATA/reardon2018/scalinghcp/civet/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-reardon2018_desc-scalinghcp_space-civet_den-41k_hemi-L_feature.func.gii

**References**
    - PK Reardon, Jakob Seidlitz, Simon Vandekar, Siyuan Liu, Raihaan Patel, Min Tae M Park, Aaron Alexander-Bloch, Liv S Clasen, Jonathan D Blumenthal, Francois M Lalonde, and others. Normative brain size variation and brain shape diversity in humans. Science, 360(6394):1222–1227, 2018.

----

reardon2018-scalingnih-civet-41k
================================

**Annotation identifier**

*{'source': 'reardon2018', 'desc': 'scalingnih', 'space': 'civet', 'den': '41k'}*

**Full description**

Cortical areal scaling during development from the NIH dataset

**Demographics**: N = 1531, Age =  5-25

**Tags**: structural, MRI

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='reardon2018', desc='scalingnih', space='civet', den='41k')

    # describe annotation
    describe_annotations(('reardon2018', 'scalingnih', 'civet', '41k'))

    # file location
    # $NEUROMAPS_DATA/reardon2018/scalingnih/civet/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-reardon2018_desc-scalingnih_space-civet_den-41k_hemi-L_feature.func.gii

**References**
    - PK Reardon, Jakob Seidlitz, Simon Vandekar, Siyuan Liu, Raihaan Patel, Min Tae M Park, Aaron Alexander-Bloch, Liv S Clasen, Jonathan D Blumenthal, Francois M Lalonde, and others. Normative brain size variation and brain shape diversity in humans. Science, 360(6394):1222–1227, 2018.

----

reardon2018-scalingpnc-civet-41k
================================

**Annotation identifier**

*{'source': 'reardon2018', 'desc': 'scalingpnc', 'space': 'civet', 'den': '41k'}*

**Full description**

Cortical areal scaling during development from the PNC dataset

**Demographics**: N = 1373, Age =  8-23

**Tags**: structural, MRI

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='reardon2018', desc='scalingpnc', space='civet', den='41k')

    # describe annotation
    describe_annotations(('reardon2018', 'scalingpnc', 'civet', '41k'))

    # file location
    # $NEUROMAPS_DATA/reardon2018/scalingpnc/civet/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-reardon2018_desc-scalingpnc_space-civet_den-41k_hemi-L_feature.func.gii

**References**
    - PK Reardon, Jakob Seidlitz, Simon Vandekar, Siyuan Liu, Raihaan Patel, Min Tae M Park, Aaron Alexander-Bloch, Liv S Clasen, Jonathan D Blumenthal, Francois M Lalonde, and others. Normative brain size variation and brain shape diversity in humans. Science, 360(6394):1222–1227, 2018.

----

rosaneto-abp688-MNI152-1mm
==========================

**Annotation identifier**

*{'source': 'rosaneto', 'desc': 'abp688', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (BPnd) to mGluR5 (glutamate receptor)

**Demographics**: N = 22, Age = 67.9 +/- 9.6

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='rosaneto', desc='abp688', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('rosaneto', 'abp688', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/rosaneto/abp688/MNI152

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-rosaneto_desc-abp688_space-MNI152_res-1mm_feature.nii.gz

**References**
    - Justine Y Hansen, Golia Shafiei, Ross D Markello, Kelly Smart, Sylvia ML Cox, Martin Nørgaard, Vincent Beliveau, Yanjun Wu, Jean-Dominique Gallezot, Étienne Aumont, and others. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. Nature neuroscience, 25(11):1569–1581, 2022.

----

sandiego2015-flb457-MNI152-1mm
==============================

**Annotation identifier**

*{'source': 'sandiego2015', 'desc': 'flb457', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (BPnd) to D2 (dopamine receptor)

**Demographics**: N = 55, Age = 32.45 +/- 9.69

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='sandiego2015', desc='flb457', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('sandiego2015', 'flb457', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/sandiego2015/flb457/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-sandiego2015_desc-flb457_space-MNI152_res-1mm_feature.nii.gz

**References**
    - Christine M Sandiego, Jean-Dominique Gallezot, Keunpoong Lim, Jim Ropchan, Shu-fei Lin, Hong Gao, Evan D Morris, and Kelly P Cosgrove. Reference region modeling approaches for amphetamine challenge studies with [11c] flb 457 and pet. Journal of Cerebral Blood Flow & Metabolism, 35(4):623–629, 2015.
    - Justine Y Hansen, Golia Shafiei, Ross D Markello, Kelly Smart, Sylvia ML Cox, Martin Nørgaard, Vincent Beliveau, Yanjun Wu, Jean-Dominique Gallezot, Étienne Aumont, and others. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. Nature neuroscience, 25(11):1569–1581, 2022.
    - Christopher T Smith, Jennifer L Crawford, Linh C Dang, Kendra L Seaman, M Danica San Juan, Aishwarya Vijay, Daniel T Katz, David Matuskey, Ronald L Cowan, Evan D Morris, and others. Partial-volume correction increases estimated dopamine d2-like receptor binding potential and reduces adult age differences. Journal of Cerebral Blood Flow & Metabolism, 39(5):822–833, 2019.
    - Yasmin Zakiniaeiz, Ansel T Hillmer, David Matuskey, Nabeel Nabulsi, Jim Ropchan, Carolyn M Mazure, Marina R Picciotto, Yiyun Huang, Sherry A McKee, Evan D Morris, and others. Sex differences in amphetamine-induced dopamine release in the dorsolateral prefrontal cortex of tobacco smokers. Neuropsychopharmacology, 44(13):2205–2211, 2019.
    - Mark Slifstein, Elsmarieke Van De Giessen, Jared Van Snellenberg, Judy L Thompson, Rajesh Narendran, Roberto Gil, Elizabeth Hackett, Ragy Girgis, Najate Ojeil, Holly Moore, and others. Deficits in prefrontal cortical and extrastriatal dopamine release in schizophrenia: a positron emission tomographic functional magnetic resonance imaging study. JAMA psychiatry, 72(4):316–324, 2015.
    - Christine M Sandiego, David Matuskey, Meaghan Lavery, Erin McGovern, Yiyun Huang, Nabeel Nabulsi, Jim Ropchan, Marina R Picciotto, Evan D Morris, Sherry A McKee, and others. The effect of treatment with guanfacine, an alpha2 adrenergic agonist, on dopaminergic tone in tobacco smokers: an [11 c] flb457 pet study. Neuropsychopharmacology, 43(5):1052–1058, 2018.

----

sasaki2012-fepe2i-MNI152-1mm
============================

**Annotation identifier**

*{'source': 'sasaki2012', 'desc': 'fepe2i', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (BPnd) to DAT (dopamine transporter)

**Demographics**: N = 6, Age = 31.06 +/- 7.7

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='sasaki2012', desc='fepe2i', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('sasaki2012', 'fepe2i', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/sasaki2012/fepe2i/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-sasaki2012_desc-fepe2i_space-MNI152_res-1mm_feature.nii.gz

**References**
    - Takeshi Sasaki, Hiroshi Ito, Yasuyuki Kimura, Ryosuke Arakawa, Harumasa Takano, Chie Seki, Fumitoshi Kodaka, Saori Fujie, Keisuke Takahata, Tsuyoshi Nogami, and others. Quantification of dopamine transporter in human brain using pet with 18f-fe-pe2i. Journal of Nuclear Medicine, 53(7):1065–1073, 2012.

----

satterthwaite2014-meancbf-MNI152-1mm
====================================

**Annotation identifier**

*{'source': 'satterthwaite2014', 'desc': 'meancbf', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

Cerebral blood flow

**Demographics**: N = 922, Age =  8-22

**Tags**: functional, ASL

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='satterthwaite2014', desc='meancbf', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('satterthwaite2014', 'meancbf', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/satterthwaite2014/meancbf/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-satterthwaite2014_desc-meancbf_space-MNI152_res-1mm_feature.nii.gz

**References**
    - Theodore D Satterthwaite, Russell T Shinohara, Daniel H Wolf, Ryan D Hopson, Mark A Elliott, Simon N Vandekar, Kosha Ruparel, Monica E Calkins, David R Roalf, Efstathios D Gennatas, and others. Impact of puberty on the evolution of cerebral perfusion during adolescence. Proceedings of the National Academy of Sciences, 111(23):8643–8648, 2014.

----

savli2012-altanserin-MNI152-3mm
===============================

**Annotation identifier**

*{'source': 'savli2012', 'desc': 'altanserin', 'space': 'MNI152', 'res': '3mm'}*

**Full description**

PET tracer binding (BPnd) to 5-HT2a (serotonin receptor)

**Demographics**: N = 19, Age = 28.2 +/- 5.7

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='savli2012', desc='altanserin', space='MNI152', res='3mm')

    # describe annotation
    describe_annotations(('savli2012', 'altanserin', 'MNI152', '3mm'))

    # file location
    # $NEUROMAPS_DATA/savli2012/altanserin/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-savli2012_desc-altanserin_space-MNI152_res-3mm_feature.nii.gz

**References**
    - Markus Savli, Andreas Bauer, Markus Mitterhauser, Yu-Shin Ding, Andreas Hahn, Tina Kroll, Alexander Neumeister, Daniela Haeusler, Johanna Ungersboeck, Shannan Henry, and others. Normative database of the serotonergic system in healthy subjects using multi-tracer pet. Neuroimage, 63(1):447–459, 2012.

----

savli2012-dasb-MNI152-3mm
=========================

**Annotation identifier**

*{'source': 'savli2012', 'desc': 'dasb', 'space': 'MNI152', 'res': '3mm'}*

**Full description**

PET tracer binding (BPnd) to 5-HTT (serotonin transporter)

**Demographics**: N = 18, Age = 30.5 +/- 9.5

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='savli2012', desc='dasb', space='MNI152', res='3mm')

    # describe annotation
    describe_annotations(('savli2012', 'dasb', 'MNI152', '3mm'))

    # file location
    # $NEUROMAPS_DATA/savli2012/dasb/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-savli2012_desc-dasb_space-MNI152_res-3mm_feature.nii.gz

**References**
    - Markus Savli, Andreas Bauer, Markus Mitterhauser, Yu-Shin Ding, Andreas Hahn, Tina Kroll, Alexander Neumeister, Daniela Haeusler, Johanna Ungersboeck, Shannan Henry, and others. Normative database of the serotonergic system in healthy subjects using multi-tracer pet. Neuroimage, 63(1):447–459, 2012.

----

savli2012-p943-MNI152-3mm
=========================

**Annotation identifier**

*{'source': 'savli2012', 'desc': 'p943', 'space': 'MNI152', 'res': '3mm'}*

**Full description**

PET tracer binding (BPnd) to 5-HT1b (serotonin receptor)

**Demographics**: N = 23, Age = 28.7 +/- 7

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='savli2012', desc='p943', space='MNI152', res='3mm')

    # describe annotation
    describe_annotations(('savli2012', 'p943', 'MNI152', '3mm'))

    # file location
    # $NEUROMAPS_DATA/savli2012/p943/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-savli2012_desc-p943_space-MNI152_res-3mm_feature.nii.gz

**References**
    - Markus Savli, Andreas Bauer, Markus Mitterhauser, Yu-Shin Ding, Andreas Hahn, Tina Kroll, Alexander Neumeister, Daniela Haeusler, Johanna Ungersboeck, Shannan Henry, and others. Normative database of the serotonergic system in healthy subjects using multi-tracer pet. Neuroimage, 63(1):447–459, 2012.

----

savli2012-way100635-MNI152-3mm
==============================

**Annotation identifier**

*{'source': 'savli2012', 'desc': 'way100635', 'space': 'MNI152', 'res': '3mm'}*

**Full description**

PET tracer binding (BPnd) to 5-HT1a (serotonin receptor)

**Demographics**: N = 35, Age = 26.3 +/- 5.2

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='savli2012', desc='way100635', space='MNI152', res='3mm')

    # describe annotation
    describe_annotations(('savli2012', 'way100635', 'MNI152', '3mm'))

    # file location
    # $NEUROMAPS_DATA/savli2012/way100635/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-savli2012_desc-way100635_space-MNI152_res-3mm_feature.nii.gz

**References**
    - Markus Savli, Andreas Bauer, Markus Mitterhauser, Yu-Shin Ding, Andreas Hahn, Tina Kroll, Alexander Neumeister, Daniela Haeusler, Johanna Ungersboeck, Shannan Henry, and others. Normative database of the serotonergic system in healthy subjects using multi-tracer pet. Neuroimage, 63(1):447–459, 2012.

----

smart2019-abp688-MNI152-1mm
===========================

**Annotation identifier**

*{'source': 'smart2019', 'desc': 'abp688', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (BPnd) to mGluR5 (glutamate receptor)

**Demographics**: N = 73, Age = 19.9 +/- 3.04

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='smart2019', desc='abp688', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('smart2019', 'abp688', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/smart2019/abp688/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-smart2019_desc-abp688_space-MNI152_res-1mm_feature.nii.gz

**References**
    - Kelly Smart, Sylvia ML Cox, Stephanie G Scala, Maria Tippler, Natalia Jaworska, Michel Boivin, Jean R Séguin, Chawki Benkelfat, and Marco Leyton. Sex differences in [11 c] abp688 binding: a positron emission tomography study of mglu5 receptors. European journal of nuclear medicine and molecular imaging, 46(5):1179–1183, 2019.
    - Justine Y Hansen, Golia Shafiei, Ross D Markello, Kelly Smart, Sylvia ML Cox, Martin Nørgaard, Vincent Beliveau, Yanjun Wu, Jean-Dominique Gallezot, Étienne Aumont, and others. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. Nature neuroscience, 25(11):1569–1581, 2022.

----

smith2017-flb457-MNI152-1mm
===========================

**Annotation identifier**

*{'source': 'smith2017', 'desc': 'flb457', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (BPnd) to D2 (dopamine receptor)

**Demographics**: N = 37, Age = 48.36 +/- 16.93

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='smith2017', desc='flb457', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('smith2017', 'flb457', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/smith2017/flb457/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-smith2017_desc-flb457_space-MNI152_res-1mm_feature.nii.gz

**References**
    - Christopher T Smith, Jennifer L Crawford, Linh C Dang, Kendra L Seaman, M Danica San Juan, Aishwarya Vijay, Daniel T Katz, David Matuskey, Ronald L Cowan, Evan D Morris, and others. Partial-volume correction increases estimated dopamine d2-like receptor binding potential and reduces adult age differences. Journal of Cerebral Blood Flow & Metabolism, 39(5):822–833, 2019.

----

spreng-feobv-MNI152-1mm
=======================

**Annotation identifier**

*{'source': 'spreng', 'desc': 'feobv', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (SUVR) to VAChT (acetylcholine transporter)

**Demographics**: N = 3, Age = 66.6 +/- 0.94

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='spreng', desc='feobv', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('spreng', 'feobv', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/spreng/feobv/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-spreng_desc-feobv_space-MNI152_res-1mm_feature.nii.gz

**References**
    - Justine Y Hansen, Golia Shafiei, Ross D Markello, Kelly Smart, Sylvia ML Cox, Martin Nørgaard, Vincent Beliveau, Yanjun Wu, Jean-Dominique Gallezot, Étienne Aumont, and others. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. Nature neuroscience, 25(11):1569–1581, 2022.

----

sydnor2021-SAaxis-fsLR-32k
==========================

**Annotation identifier**

*{'source': 'sydnor2021', 'desc': 'SAaxis', 'space': 'fsLR', 'den': '32k'}*

**Full description**

Sensory-association mean rank axis

**Demographics**: N = 3, Age = 66.6 +/- 0.94

**Tags**: MRI

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='sydnor2021', desc='SAaxis', space='fsLR', den='32k')

    # describe annotation
    describe_annotations(('sydnor2021', 'SAaxis', 'fsLR', '32k'))

    # file location
    # $NEUROMAPS_DATA/sydnor2021/SAaxis/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-sydnor2021_desc-SAaxis_space-fsLR_den-32k_hemi-L_feature.func.gii

**References**
    - Valerie J Sydnor, Bart Larsen, Danielle S Bassett, Aaron Alexander-Bloch, Damien A Fair, Conor Liston, Allyson P Mackey, Michael P Milham, Adam Pines, David R Roalf, and others. Neurodevelopment of the association cortices: patterns, mechanisms, and implications for psychopathology. Neuron, 109(18):2820–2846, 2021.

----

tuominen-feobv-MNI152-2mm
=========================

**Annotation identifier**

*{'source': 'tuominen', 'desc': 'feobv', 'space': 'MNI152', 'res': '2mm'}*

**Full description**

PET tracer binding (SUVR) to VAChT (acetylcholine transporter)

**Demographics**: N = 4, Age = 37 +/- 10.2

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='tuominen', desc='feobv', space='MNI152', res='2mm')

    # describe annotation
    describe_annotations(('tuominen', 'feobv', 'MNI152', '2mm'))

    # file location
    # $NEUROMAPS_DATA/tuominen/feobv/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-tuominen_desc-feobv_space-MNI152_res-2mm_feature.nii.gz

**References**
    - Justine Y Hansen, Golia Shafiei, Ross D Markello, Kelly Smart, Sylvia ML Cox, Martin Nørgaard, Vincent Beliveau, Yanjun Wu, Jean-Dominique Gallezot, Étienne Aumont, and others. Mapping neurotransmitter systems to the structural and functional organization of the human neocortex. Nature neuroscience, 25(11):1569–1581, 2022.

----

turtonen2020-carfentanil-MNI152-1mm
===================================

**Annotation identifier**

*{'source': 'turtonen2020', 'desc': 'carfentanil', 'space': 'MNI152', 'res': '1mm'}*

**Full description**

PET tracer binding (BPnd) to MOR (mu-opioid receptor)

**Demographics**: N = 39, Age = 39.38 +/- 5.05

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='turtonen2020', desc='carfentanil', space='MNI152', res='1mm')

    # describe annotation
    describe_annotations(('turtonen2020', 'carfentanil', 'MNI152', '1mm'))

    # file location
    # $NEUROMAPS_DATA/turtonen2020/carfentanil/MNI152/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-turtonen2020_desc-carfentanil_space-MNI152_res-1mm_feature.nii.gz

**References**
    - Otto Turtonen, Aino Saarinen, Lauri Nummenmaa, Lauri Tuominen, Maria Tikka, Reetta-Liina Armio, Airi Hautamäki, Heikki Laurikainen, Olli Raitakari, Liisa Keltikangas-Järvinen, and others. Adult attachment system links with brain mu opioid receptor availability in vivo. Biological Psychiatry: Cognitive Neuroscience and Neuroimaging, 6(3):360–369, 2021.

----

vijay2018-ly2795050-MNI152-2mm
==============================

**Annotation identifier**

*{'source': 'vijay2018', 'desc': 'ly2795050', 'space': 'MNI152', 'res': '2mm'}*

**Full description**

PET tracer binding (Vt) to KOR (kappa-opioid receptor)

**Demographics**: N = 28, Age = 33.5 +/- 11.3

**Tags**: receptors, PET

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='vijay2018', desc='ly2795050', space='MNI152', res='2mm')

    # describe annotation
    describe_annotations(('vijay2018', 'ly2795050', 'MNI152', '2mm'))

    # file location
    # $NEUROMAPS_DATA/vijay2018/ly2795050/MNI152

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-vijay2018_desc-ly2795050_space-MNI152_res-2mm_feature.nii.gz

**References**
    - Aishwarya Vijay, Dana Cavallo, Alissa Goldberg, Bart de Laat, Nabeel Nabulsi, Yiyun Huang, Suchitra Krishnan-Sarin, and Evan D Morris. Pet imaging reveals lower kappa opioid receptor availability in alcoholics but no effect of age. Neuropsychopharmacology, 43(13):2539–2547, 2018.

----

xu2020-FChomology-fsLR-32k
==========================

**Annotation identifier**

*{'source': 'xu2020', 'desc': 'FChomology', 'space': 'fsLR', 'den': '32k'}*

**Full description**

Cross-species functional homology

**Demographics**: N = None, Age = None

**Tags**: functional, MRI

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='xu2020', desc='FChomology', space='fsLR', den='32k')

    # describe annotation
    describe_annotations(('xu2020', 'FChomology', 'fsLR', '32k'))

    # file location
    # $NEUROMAPS_DATA/xu2020/FChomology/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-xu2020_desc-FChomology_space-fsLR_den-32k_hemi-R_feature.func.gii

**References**
    - Ting Xu, Karl-Heinz Nenning, Ernst Schwartz, Seok-Jun Hong, Joshua T Vogelstein, Alexandros Goulas, Damien A Fair, Charles E Schroeder, Daniel S Margulies, Jonny Smallwood, and others. Cross-species functional alignment reveals evolutionary hierarchy within the connectome. Neuroimage, 223:117346, 2020.

----

xu2020-evoexp-fsLR-32k
======================

**Annotation identifier**

*{'source': 'xu2020', 'desc': 'evoexp', 'space': 'fsLR', 'den': '32k'}*

**Full description**

Evolutionary cortical expansion

**Demographics**: N = None, Age = None

**Tags**: structural, MRI

**How to use**

.. code:: python

    # get annotation
    fetch_annotation(source='xu2020', desc='evoexp', space='fsLR', den='32k')

    # describe annotation
    describe_annotations(('xu2020', 'evoexp', 'fsLR', '32k'))

    # file location
    # $NEUROMAPS_DATA/xu2020/evoexp/fsLR/

    # file name (for surface data, replace L/R to get the other hemisphere)
    # source-xu2020_desc-evoexp_space-fsLR_den-32k_hemi-R_feature.func.gii

**References**
    - Ting Xu, Karl-Heinz Nenning, Ernst Schwartz, Seok-Jun Hong, Joshua T Vogelstein, Alexandros Goulas, Damien A Fair, Charles E Schroeder, Daniel S Margulies, Jonny Smallwood, and others. Cross-species functional alignment reveals evolutionary hierarchy within the connectome. Neuroimage, 223:117346, 2020.