The problem: detecting changes on server.

The idea is to recursively traverse a web-site, download certain files (whose name or path doesn't contain stop words) and check if their md5 checksums differ from the local version.

The realization relies on having Producer put the links to files into a Queue without size limit, while consumers would download the files and get all the work. Then tune the number of consumers to balance the speed, queue size and the hard drive usage.