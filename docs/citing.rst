.. _citation:

-------------
Citing neuromaps
-------------

We're thrilled you've found ``neuromaps`` useful in your work! Please cite the
following manuscripts when referencing your use of the toolbox:

1. Markello, RD, Hansen, JY, Liu, ZQ, Bazinet, V, Shafiei, G, Suarez, LE, 
   Blostein, N, Seidlitz, J, Baillet, S, Satterthwaite, TD & Chakravarty, M. 
   (2022). Neuromaps: structural and functional interpretation of brain maps. 
   Biorxiv. doi:`10.1101/bioRxiv.475081 <https://doi.org/10.1101/2022.01.06.475081>`__

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
paper that published this data. The first item of the annotation (the source) will 
represent the last name of the first author and the year of publication. Alternatively, 
the source may be a toolbox. Most citations can be found in the `preprint <https://www.biorxiv.org/content/10.1101/2022.01.06.475081v1>`_ 

For more information about why citing software is important please refer to
`this article <https://www.software.ac.uk/how-cite-software>`_ from the
Software Sustainability Institute.

.. _DOI: https://en.wikipedia.org/wiki/Digital_object_identifier
.. _Zenodo: https://zenodo.org