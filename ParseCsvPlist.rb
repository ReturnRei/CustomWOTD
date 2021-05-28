require 'csv'
require 'nokogiri'

voc=[]
CSV.foreach("N5-N3.csv", col_sep: ';') do |row|
  voc << row
end

xml = Nokogiri::XML::Builder.new(:encoding => 'UTF-8') { |xml|
  xml.root  do
    for i in 0..1065
  xml.dict do
      xml.key_ "DCSWotDEntryHeadword"
      xml.string voc[i][0]
      xml.key_ "DCSWotDEntrySecondaryHeadword"
      xml.string voc[i][1]
      xml.key_ "DCSWotDEntrySense"
      xml.string voc[i][2]
  end
  end
  end
}.to_xml

puts xml