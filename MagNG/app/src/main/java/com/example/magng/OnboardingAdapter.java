package com.example.magng;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class OnboardingAdapter extends RecyclerView.Adapter<OnboardingAdapter.OnboardingViewHolder>{

    private List<OnboardingItem> onboardingItems;

    public OnboardingAdapter(List<OnboardingItem> onboardingItems) {
        this.onboardingItems = onboardingItems;
    }

    @NonNull
    @Override
    public OnboardingViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        return new OnboardingViewHolder(
                LayoutInflater.from(parent.getContext()).inflate(R.layout.onboarding_items, parent,
                        false)
        );
    }

    @Override
    public void onBindViewHolder(@NonNull OnboardingViewHolder holder, int position) {
        holder.setOnboardingData(onboardingItems.get(position));

    }

    @Override
    public int getItemCount() {

        return onboardingItems.size();
    }

    class OnboardingViewHolder extends RecyclerView.ViewHolder {
        private ImageView imageOnBoarding;
        private TextView textDescription;

         public OnboardingViewHolder(@NonNull View itemView) {
            super(itemView);
            imageOnBoarding = itemView.findViewById(R.id.imageOnBoarding);
            textDescription = itemView.findViewById(R.id.textDescription);

        }
        void setOnboardingData(OnboardingItem onboardingItem){
            textDescription.setText(onboardingItem.getTextDescription());
            imageOnBoarding.setImageResource(onboardingItem.getImage());
        }
    }

}
