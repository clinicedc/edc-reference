# edc-reference

[![Build Status](https://travis-ci.com/clinicedc/edc-reference.svg?branch=develop)](https://travis-ci.com/clinicedc/edc-reference) [![Coverage Status](https://coveralls.io/repos/github/clinicedc/edc-reference/badge.svg?branch=develop)](https://coveralls.io/github/clinicedc/edc-reference?branch=develop)

pivoted reference table for EDC modules

`edc_reference` creates a pivoted table of CRF and Requisition records with a small subset of values that can be efficiently referenced. The module is used by `edc_metadata_rules` to quickly determine if a CRF or Requisition model instance exists avoiding the need to query each individual model class.

See also `edc_metadata_rules`


## Usage and Configuration

Declare a model with the `ReferenceModelMixin`.

    from edc_reference.model_mixins import ReferenceModelMixin

    class CrfOne(ReferenceModelMixin, BaseUuidModel):
    
        subject_visit = models.ForeignKey(SubjectVisit, on_delete=PROTECT)
    
        report_datetime = models.DateTimeField(default=get_utcnow)
    
        f1 = models.CharField(max_length=50)
        
        f2 = models.CharField(max_length=50)
        
        f3 = models.CharField(max_length=50)
        
        f4 = models.DatetimeField(null=True)

        
Register the model and the relevant fields with the site global, `site_reference_configs`:

    from edc_reference.site import ReferenceModelConfig

    reference = ReferenceModelConfig(
        model='edc_reference.crfone',
        fields=['f1', 'f4'])
    site_reference_configs.register(reference)
        
Create a model instance:

    crf_one = CrfOne.objects.create(
        subject_visit=subject_visit,
        f1='happiness'
        f4=get_utcnow())
        
The `Reference` model will be updated:


    from edc_reference.models import Reference
    
    reference = Reference.objects.get(
        identifier=self.subject_identifier,
        timepoint=self.subject_visit.visit_code,
        report_datetime=crf_one.report_datetime,
        field_name='f1')
        
    >>> reference.__dict__
    { ...
     'datatype': 'CharField',
     'field_name': 'f1',
     'identifier': '1',
     'model': 'edc_reference.crfone',
     'report_datetime': datetime.datetime(2017, 7, 7, 13, 30, 6, 545140, tzinfo=<UTC>),
     'timepoint': 'code',
     'value_date': None,
     'value_datetime': None,
     'value_int': None,
     'value_str': 'happiness',
     ...}    
 
 
Get the `value` from the reference instance:
 
    >>> reference.value
    'happiness'
    
Model managers methods are also available, for example:

    reference = Reference.objects.crf_get_for_visit(
        model='edc_reference.crfone', 
        visit=self.subject_visit,
        field_name='f1')
    
    >>> reference.value
    'happiness'
     
 
### Accessing pivoted data with `LongitudinalRefset`



    
