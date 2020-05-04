% Function to return the sigmoid value of input
function g = sigmoid(z)

g = zeros(size(z));
g = 1./(1+exp(-z));
    
end
