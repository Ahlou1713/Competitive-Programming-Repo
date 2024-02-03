class Solution:
    def defangIPaddr(self, address: str) -> str:
        #The function 'replace' replaces the first given string by the second given string
        return address.replace('.','[.]')