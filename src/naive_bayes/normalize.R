orig_data = read.csv("melanoma_data.csv", sep=",", header=FALSE)

normalize = function(xs){(xs - mean(xs))/sd(xs)}
norm_data = orig_data
norm_data$V129<-NULL
norm_data = as.data.frame(apply(norm_data, 2, normalize))
norm_data$V129 = orig_data$V129
write.csv(norm_data, "melanoma_normalized_data.csv", row.names=FALSE)

prob_data = read.csv("probabilities.csv", sep=",", header=FALSE)

normalize = function(xs){(xs - mean(xs))/sd(xs)}
norm_data = prob_data
norm_data = as.data.frame(apply(norm_data, 2, normalize))
norm_data$V1 = prob_data$V1
write.csv(norm_data, "prob_normalized_data.csv", row.names=FALSE)
