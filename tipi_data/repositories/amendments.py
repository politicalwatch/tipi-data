from tipi_data.models.amendment import Amendment

class Amendments:

   @staticmethod 
   def by_reference(reference):
        return Amendment.objects.filter(reference=reference)

   @staticmethod 
   def by_reference_and_bulletin(reference, bulletin):
        return Amendment.objects.filter(reference=reference, bulletin_name=bulletin)

   @staticmethod
   def get_all_untagged():
       query = {
               '$or': [
                   {'justification_tagged': []},
                   {'justification_tagged': {'$exists': False}},
                   {'propossed_change_tagged': []},
                   {'propossed_change_tagged': {'$exists': False}},
                   ]
               }
       return Amendments.by_query(query)

   @staticmethod
   def by_query(query):
       if '$text' in query.keys():
           return Amendment.objects(__raw__=query).order_by()

       return Amendment.objects(__raw__=query)
