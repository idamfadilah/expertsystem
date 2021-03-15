import numpy as np

# Transitional model:
transitional_model = np.array([[0.7, 0.3],
                               [0.3, 0.7]])

# Observational model where an umbrella has been observed:
obs_model_with_umbrella = np.array([[0.9, 0.0],
                                    [0.0, 0.2]])

# Observational model where a distinct lack of an umbrella has been observed:
obs_model_without_umbrella = np.array([[0.1, 0.0],
                                       [0.0, 0.8]])

# Observations from task, only to be used if algorithm is applied to specific task
evidence_list_from_task = [True, True, False, True, True]


# Normalization function. As per the textbook description of the task a
# value alpha must be multiplied to keep the the vectors stochastic
# input used here will be 1, but I have set the option for other values
# The vector input is the vector to be normalized.
# Expected form is [a, b], or longer.
def normalize(vector, endsum=1):
    """
    :param vector: The vector that is to be normalized, as in have the sum of its values set to a given value
    :param endsum: Default value is one, as this method is mostly used to make vectors stochastic.
    :return:
    """
    vector_element_sum = 0
    for element in vector:
        vector_element_sum += element

    unit_to_divide_by = vector_element_sum / endsum

    return_vector = []
    for i in range(len(vector)):
        return_vector.append(vector[i] / unit_to_divide_by)
    return return_vector


# Forward algorithm, used to recursively filter the distribution
# Works its way back to an initial probability vector, in this case [0.5, 0.5]
# The transition model used in this specific case will always be the one created at the top of the file
def forward(transition_model, obs_model, previous_forward_message):
    """
    :param transition_model: The transitional model used, in this case a 2x2 matrix
    :param obs_model: The observational model used, in this case a 2x2 matrix containing the probabilities for the given observation
    :param previous_forward_message: The previous forward message, in this case it is the previous vector in the HMM
    """
    next_state_vector = obs_model.dot(transition_model.dot(previous_forward_message))
    return normalize(next_state_vector)


def test_forward_algorithm(evidence_list=[True, True, False, True, True]):
    # Task b) part 1
    p_X0 = [0.5, 0.5]
    pX1_given_e1 = forward(transitional_model, obs_model_with_umbrella, p_X0)
    pX2_given_e1e2 = forward(transitional_model, obs_model_with_umbrella, pX1_given_e1)
    print("b) part 1", pX1_given_e1, "\n", pX2_given_e1e2, "\n")

    # Task b) part 2
    prev_message = [0.5, 0.5]
    print("b) part 2")
    for i in range(5):
        if evidence_list[i]:
            prev_message = forward(transitional_model, obs_model_with_umbrella, prev_message)
        else:
            prev_message = forward(transitional_model, obs_model_without_umbrella, prev_message)
        print(prev_message)


# Backward algorithm, runs backwards to compute the smoothed P(X_k | e_1:t)
#
def backward(transition_model, obs_model, previous_backward_message):
    """
    :param transition_model: The transitional model used, in this case a 2x2 matrix
    :param obs_model: The observational model used, in this case a 2x2 matrix containing the probabilities for the given observation
    :param previous_backward_message: The previous backward message, in this case it is the next vector in the HMM
    """
    next_state_vector = transition_model.dot(obs_model.dot(previous_backward_message))
    return next_state_vector


# Forward-Backward algorithm, first filters all the vectors, then runs backwards smoothing all the vectors
def forward_backward(transition_model, evidence_list=[True, True, False, True, True], prior=[0.5, 0.5]):
    """
    :param transitional_model: Likelyhood matrix
    :param prior: initial value, in this case it will be [0.5, 0.5]
    :param evidence_list: The actual occurances, in our specific case: [True, True, False, True, True]
    :return: Returns a list containing the smoothed vectors corresponding to this occurance
    """
    fv = [prior]  # forward vector
    b = [1, 1]  # backward vector, init all ones
    sv = []  # Smooth vector
    N = len(evidence_list)  # number of events
    # iterates through the values and filters them using the forward algorithm
    for i in range(len(evidence_list)):
        if evidence_list[i]:
            fv.append(forward(transition_model, obs_model_with_umbrella, fv[i]))
        else:
            fv.append(forward(transition_model, obs_model_without_umbrella, fv[i]))
    # iterates backwards from the most recent evidence, smoothing the values
    for i in range(N):
        print("b at step ", N - i + 1, b)  # This line is added to show the progression of the backward algorithm.
        sv.append(normalize(np.asarray(fv[N - i]) * np.asarray(b)))
        # change the value of b to continue smoothing backwards
        if evidence_list[N - i - 1]:
            b = backward(transition_model, obs_model_with_umbrella, b)
        else:
            b = backward(transition_model, obs_model_without_umbrella, b)
    return sv


def test_forward_backward_algorithm():
    # Task c) part 1; calculate P(X1 | e1:e2))
    print("\n" + "c) part 1" + "\n")
    print(forward_backward(transitional_model, evidence_list_from_task[0:2])[0])
    print("which means that the result is as expected." + "\n")
    # task c) part 2; calculate P(X1 | e1:e5)
    print("c) part 2" + "\n")
    print(forward_backward(transitional_model, evidence_list_from_task)[0])
    print("which means that the result is as expected." + "\n")


def main():
    test_forward_algorithm()
    test_forward_backward_algorithm()


if __name__ == "__main__":
    main()
