v_array = [
    1,
    [3,4], 
    [9,7,5]
]

result = Array.new 

v_array.each do |i|
    if i.is_a? Array then
        i.each do |k|
            result.insert(-1, k)
        end
    else
        result.insert(-1, i)
    end
end

result = result.sort

result.each do |j|
    puts "#{j}\n"
end