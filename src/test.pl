# use Inline Python;

my $str1 = "Amongst the hundreds of thousands of symbols which are in the unicode text specifications are certain characters which resemble, or are variations of the alphabet and other keyword symbols. For example, if we can take the phrase and convert its characters into the fancy letters which are a set of unicode symbols. These different sets of fancy text letters are scattered all throughout the unicode specification, and so to create a fancy text translator, it's just a matter of finding these sets of letters and symbols, and linking them to their normal alphabetical equivalents.";

my $str2 = "After generating your fancy text symbols, you can copy and paste the to most websites and text processors. You could use it to generate a fancy Agario name (yep, weird text in agario is probably generated using a fancy text converter similar to this), to generate a creative-looking instagram, facebook, tumblr, or twitter post, for showing up n00bs on Steam, or just for sending messages full of beautiful text to your buddies.";

my @ret = `b.py`;

print(@ret);

# my $ret = getFeatures($str1, $str2, 2);
# print($ret);

# __END__
# __Python__
 
# from CvGenerator import getFeatures