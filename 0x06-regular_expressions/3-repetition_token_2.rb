#!/usr/bin/env ruby
# Ruby script that accepts one argument and
# pass it to a regularexpression matching method
puts ARGV[0].scan(/hbt{1,4}n/).join