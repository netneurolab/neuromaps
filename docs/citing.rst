.. _citation:

-------------
Citing neuromaps
-------------

We're thrilled you've found ``neuromaps`` useful in your work! Please cite the
following manuscripts when referencing your use of the toolbox:

1. Markello, RD, Hansen, JY, Liu, ZQ, Bazinet, V, Shafiei, G, Suarez, LE, 
   Blostein, N, Seidlitz, J, Baillet, S, Satterthwaite, TD, Chakravarty, MM, Raznahan, A, Misic, B. 
   (2022). neuromaps: structural and functional interpretation of brain maps. 
   Nature Methods. doi:`10.1038/s41592-022-01625-w <https://doi.org/10.1038/s41592-022-01625-w>`__
2. If you use volume-to-surface transformations (registration fusion), please cite `Buckner et al 2011    <https://journals.physiology.org/doi/full/10.1152/jn.00339.2011>`_ (original proposition) and `Wu et al 2018 <https://onlinelibrary.wiley.com/doi/10.1002/hbm.24213>`_ (first implementation of MNI152 to fsaverage transformation).
3. If you use surface-to-surface transformations (multimodal surface matching), please cite `Robinson et  al 2014 <https://www.sciencedirect.com/science/article/pii/S1053811914004546?via%3Dihub>`_ and `Robinson et al 2018 <https://www.sciencedirect.com/science/article/pii/S1053811917308649?via%3Dihub>`_.
4. If you use data included in ``neuromaps``, please cite the the original papers that publish the data.
A table with references for each brain map can be found in our `wiki <https://github.com/netneurolab/neuromaps/wiki>`_, or more specifically, at `this <https://docs.google.com/spreadsheets/d/1oZecOsvtQEh5pQkIf8cB6CyhPKVrQuko/edit?rtpof=true&sd=true#gid=1162991686>`_ link.
5. If you use the spatial null models, there is an associated citation with each type of null model.
They can be found in the docstring of the function, and also `here <https://netneurolab.github.io/neuromaps/api.html#module-neuromaps.nulls>`_. 


Additionally, to cite the specific version of the toolbox used in your analyses
you can use the following Zenodo reference:

.. raw:: html

    <script language="javascript">
    var version = 'latest';
    function fillCitation(){
       $('#neuromaps_version').text(version);

       function cb(err, zenodoID) {
          getCitation(zenodoID, 'vancouver-brackets-no-et-al', function(err, citation) {
             $('#neuromaps_citation').text(citation);
          });
          getDOI(zenodoID, function(err, DOI) {
             $('#neuromaps_doi_url').text('https://doi.org/' + DOI);
             $('#neuromaps_doi_url').attr('href', 'https://doi.org/' + DOI);
          });
       }

       if(version == 'latest') {
          getLatestIDFromconceptID("5842498", cb);
       } else {
          getZenodoIDFromTag("5842498", version, cb);
       }
    }
    </script>

    <p style="margin-left: 30px">
      <span id="neuromaps_citation">neuromaps</span> available from: <a id="neuromaps_doi_url" href="https://doi.org/10.5281/zenodo.5842498">10.5281/zenodo.5842498</a>.
      <img src onerror='fillCitation()' alt="" />
    </p>


.. Note that this will always point to the most recent ``neuromaps`` release; for
.. older releases please refer to the `Zenodo listing <https://zenodo.org/search?
.. page=1&size=20&q=conceptrecid:%223451463%22&sort=-version&all_versions=True>`__.

For more information about why citing software is important please refer to
`this article <https://www.software.ac.uk/how-cite-software>`_ from the
Software Sustainability Institute.

.. _DOI: https://en.wikipedia.org/wiki/Digital_object_identifier
.. _Zenodo: https://zenodo.org
