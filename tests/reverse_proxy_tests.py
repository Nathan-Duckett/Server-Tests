import requests
import unittest

# List of application names to be checked against their endpoints
application_names = [
    "traefik",
    "sonarr",
    "radarr",
    "lidarr",
    "bazarr",
    "ombi",
    "tautulli",
    "qbittorrent",
    "gitea"
]

class TestReverseProxy(unittest.TestCase):
    """
        Test cases to verify that the reverse proxy is working as expected.
        Verifies the return code from each host to ensure they are live and working.
    """
    
    def test_endpoints(self):
        """
        Test all of the endpoints from the list of application names verifying they are valid
        """
        failed = []
        for name in application_names:
            failedRequest = self.make_request(name)
            if failedRequest is not None:
                failed.append({
                    "Name": name,
                    "Code": failedRequest
                });

        if len(failed) > 0:
            msg = ""
            for failure in failed:
                msg += f"{failure['Name']} - {failure['Code']}\n"
            self.fail("Failed on requests:\n" + msg)


    
    def make_request(self, application_name):
        """
        Make a request to the specified application name returning a boolean indicating if the request
        failed to be made. This checks if the request was successful or was redirected which counts as
        a success within the system.
        """
        url = f"https://{application_name}.ndser.page"

        # Check for range of codes between 200 and 400 exclusive for valid requests.
        # This allows successful requests or redirect requests for authentication.
        try:
            r = requests.get(url, timeout=1)
            if r.status_code < 200 or r.status_code > 400:
                return r.status_code
        except:
            return True
        
