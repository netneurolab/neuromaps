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

If you use data included in the ``neuromaps`` repository, be sure to cite the original 
paper that published this data.
A table with references for each brain map can be found in the `Wiki <https://github.com/netneurolab/neuromaps/wiki/Annotation-information>`_.

For more information about why citing software is important please refer to
`this article <https://www.software.ac.uk/how-cite-software>`_ from the
Software Sustainability Institute.

.. _DOI: https://en.wikipedia.org/wiki/Digital_object_identifier
.. _Zenodo: https://zenodo.org
