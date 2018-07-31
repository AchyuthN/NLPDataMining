install.packages('ISLR')
library(ISLR)
str(Caravan)
purchase <- Caravan$Purchase
standard_caravan <- scale(Caravan[-86])
test_index <- 1:1000
test_data <- standard_caravan[test_index,]
test_data_purchase <- purchase[test_index]
train_data <- standard_caravan[-test_index,]
train_data_purchase <- purchase[-test_index]
#Importing class libraries which contains knn algorithms
library(class)
set.seed(101)
forecast_purchase <- knn(train_data,test_data,train_data_purchase,k=1)
print(head(forecast_purchase))
misclassification_error <- mean(test_data_purchase != forecast_purchase)
print(misclassification_error)
error_rate <- NULL
forecast_purchase <- NULL
for (i in 1:20){
  set.seed(101)
  forecast_purchase <- knn(train_data,test_data,train_data_purchase,k=i)
  error_rate[i] <- mean(test_data_purchase != forecast_purchase)
}
print(error_rate)
install.packages('ggplot2')
library(ggplot2)
k_values <- 1:20
error_df <- data.frame(error_rate,k_values)
error_df
ggplot(error_df, aes(k_values, error_rate)) + geom_point() + geom_line(lty = 'dotted', color = 'green') 
