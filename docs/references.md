# Further reading

These references provide background for the networking concepts discussed in this repository. The simulator is a simplified teaching model; the standards and platform documentation describe broader behavior.

- **RFC 4632 — Classless Inter-domain Routing (CIDR): The Internet Address Assignment and Aggregation Plan**  
  https://www.rfc-editor.org/rfc/rfc4632  
  Background on CIDR addressing and route aggregation.

- **RFC 1812 — Requirements for IP Version 4 Routers**  
  https://www.rfc-editor.org/rfc/rfc1812  
  Standards-track requirements and behavior for IPv4 routers.

- **Python `ipaddress` documentation**  
  https://docs.python.org/3/library/ipaddress.html  
  The standard-library API used by this project to parse IPv4 addresses and networks.

- **Python `unittest` documentation**  
  https://docs.python.org/3/library/unittest.html  
  Framework used by the repository's automated tests.

- **Wireshark User's Guide**  
  https://www.wireshark.org/docs/wsug_html_chunked/  
  Reference for capture workflows and display filters.

- **Cisco IOS IP Routing documentation**  
  https://www.cisco.com/c/en/us/support/ios-nx-os-software/ios-software-releases-12-2-mainline/series.html  
  Platform-specific behavior depends on product and software release. Consult the documentation matching your lab device.

## Reading advice

Start with CIDR and the IPv4 router requirements, then run the project examples. When comparing a real router, consult the exact platform's documentation instead of assuming that the simulator models every route-selection stage.
