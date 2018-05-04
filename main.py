import requests
import sys

def download(url):
    """Returns the HTML source code from the given URL
        :param url: URL to get the source from.
    """
    r = requests.get(url)
    if r.status_code != 200:
        sys.stderr.write("! Error {} retrieving url {}".format(r.status_code, url))
        return None

    return r.text


if __name__ == '__main__':
    r = ""

    for x in range(10000000,99999999):
        x = str(x)

        while True:
            if len(x) < 8:
                x = "0" + x

            if len(x) == 8:
                break

        print(x)

        url = "http://147.83.52.79/cangur/login-centre/?school=" + x

        back_r = r

        if r != back_r:
            input("difference")

        r = download(url)
#        if r:
#            sys.stdout.write(r)
#        else:
#            sys.stdout.write("Nothing was retrieved.")