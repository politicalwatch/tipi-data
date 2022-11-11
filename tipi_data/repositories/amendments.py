from tipi_data.models.amendment import Amendment

class Amendments:

   @staticmethod 
   def by_reference(reference):
        return Amendment.objects.filter(reference=reference)

   @staticmethod 
   def by_reference_and_bulletin(reference, bulletin):
        return Amendment.objects.filter(reference=reference, bulletin_name=bulletin)
